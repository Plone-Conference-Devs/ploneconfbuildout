import urllib, urllib2
import socket
import logging
import re

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.component import getUtility

from getpaid.core.interfaces import IOrderManager

from getpaid.paypal.interfaces import IPaypalStandardOptions
from getpaid.paypal.paypal import _sites

from notification import Notification

logger = logging.getLogger("Plone")

class IPNListener(BrowserView):
    """Listener for Paypal IPN notifications - registered as a page view
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.portal = getToolByName(self.context, 'portal_url').getPortalObject()
    
    def process(self):
        this_notification = Notification(self.request)
        is_valid_IPN = self.verify()
        if not is_valid_IPN:
            logger.info('getpaid.paypal: received bogus IPN')
            return
        order_manager = getUtility(IOrderManager)
        if this_notification.invoice in order_manager:
            order = order_manager.get(this_notification.invoice)
            if not self.compare_cart(this_notification, order):
                logger.info('getpaid.paypal: received IPN that does match order number %s' % this_notification.invoice)
                # bad IPN - do not apply to transaction
                return
            if this_notification.payment_status == 'Completed':
                self.fill_in_order_data(this_notification, order)
                order.finance_workflow.fireTransition('charge-charging')
                logger.info('getpaid.paypal: received successful IPN payment notification for order %s' % this_notification.invoice)
                return
            if this_notification.payment_status == 'Failed':
                order.finance_workflow.fireTransition('decline-charging')
                logger.info('getpaid.paypal: received unsuccessful IPN payment notification for order %s' % this_notification.invoice)
                return
            # IPN not of interest to us right now
            logger.info('getpaid.paypal: received IPN for order %s that is not of interest - txn_type "%s", payment_status "%s"' % (this_notification.invoice, this_notification.txn_type, this_notification.payment_status))
            return
        # invoice not in cart
        logger.info('getpaid.paypal: received IPN that does not apply to any order number - invoice "%s", txn_type "%s"' % (this_notification.invoice, this_notification.txn_type))
        return 
        
    def compare_cart(self, notification, order):
        for ref in order.shopping_cart.keys():
            cart_item = order.shopping_cart[ref]
            if notification.shopping_cart.has_key(cart_item.product_code):
                notification_item = notification.shopping_cart[cart_item.product_code]
                if int(cart_item.quantity) != int(notification_item.quantity):
                    return False
            else:
                # item not in returned cart - invalid IPN response
                return False
        # everything checks out
        return True
            


    def verify(self):
        options = IPaypalStandardOptions( self.portal )
        # get ready to POST back form variables
        
        form = self.request.form
        params =[(key, form[key]) for key in form.keys() if key != 'cmd']
        params = [('cmd', '_notify-validate')] + params
        paramData = urllib.urlencode(params)
        url = "https://%s/cgi-bin/webscr" % _sites[options.server_url]
        
        # TODO: is this dangerous for other products?
        socket.setdefaulttimeout(120)
        try:
            connection = urllib2.urlopen(url, paramData)
        except urllib2.error.URLError:
            raise IOError, 'IPN post-back failed'
        response = connection.read()
        connection.close()
               
        if response == 'VERIFIED':
            return True
        else:
            return False

    def fill_in_order_data(self, notification, order):

        name = ''
        if notification.last_name is not None and notification.first_name is not None:
            name = "%s %s" % (notification.first_name, notification.last_name)
        else:
            if notification.first_name is not None:
                name = notification.last_name
            else:
                name = notification.first_name
        order.contact_information.name = name
        
        if notification.email is not None:
            order.contact_information.email = notification.email
        
        if notification.phone is not None:
            order.contact_information.phone_number = re.sub('[^\d]+', '', notification.phone)
        
        if notification.address_street is not None:
            order.billing_address.bill_first_line = notification.address_street
        
        if notification.address_city is not None:
            order.billing_address.bill_city = notification.address_city
        
        if notification.address_state is not None:
            order.billing_address.bill_state = notification.address_state

        if notification.address_zip is not None:
            order.billing_address.bill_postal_code = notification.address_zip

        if notification.address_country is not None:
            order.billing_address.bill_country = notification.address_country

        # mark address as same - Paypal does not provide seperate shipping address
        order.shipping_address.ship_same_billing = True