"""
"""
import urllib

from Products.CMFCore.utils import getToolByName
from zope import component
from zope import interface

from interfaces import IPaypalStandardOptions, IPaypalStandardProcessor

from Products.PloneGetPaid.interfaces import IGetPaidManagementOptions
from getpaid.core import interfaces as GetPaidInterfaces

_sites = {
    "Sandbox": "www.sandbox.paypal.com",
    "Production": "www.paypal.com",
    }

class PaypalStandardProcessor( object ):
   
    interface.implements( IPaypalStandardProcessor )

    options_interface = IPaypalStandardOptions

    def __init__( self, context ):
        self.context = context

    def cart_post_button( self, order ):
        siteroot = getToolByName(self.context, "portal_url").getPortalObject()
        options = IPaypalStandardOptions( siteroot )
        manage_options = IGetPaidManagementOptions( siteroot )        
        cartitems = []
        idx = 1
        _button_form = """<form style="display:inline;" action="https://%(site)s/cgi-bin/webscr" method="post" id="paypal-button">
<input type="hidden" name="cmd" value="_cart" />
<input type="hidden" name="upload" value="1" />
<input type="hidden" name="business" value="%(merchant_id)s" />
<input type="hidden" name="currency_code" value="%(currency)s" />
<input type="hidden" name="return" value="%(return_url)s" />
<input type="hidden" name="cbt" value="Return to %(store_name)s" />
<input type="hidden" name="rm" value="2" />
<input type="hidden" name="notify_url" value="%(IPN_url)s" />
<input type="hidden" name="invoice" value="%(order_id)s" />
<input type="hidden" name="no_note" value="1" />
<input type="hidden" name="tax_cart" value="%(tax_cart)s" />
%(cart)s
<input type="image" src="http://%(site)s/en_US/i/btn/x-click-but01.gif"
    name="submit"
    alt="Make payments with PayPal - it's fast, free and secure!" />
</form>
"""
        _button_cart = """<input type="hidden" name="item_name_%(idx)s" value="%(item_name)s" />
<input type="hidden" name="item_number_%(idx)s" value="%(item_number)s" />
<input type="hidden" name="amount_%(idx)s" value="%(amount)s" />
<input type="hidden" name="quantity_%(idx)s" value="%(quantity)s" />
"""
        
        for item in order.shopping_cart.values():
            v = _button_cart % {"idx": idx,
                                "item_name": item.name,
                                "item_number" : item.product_code,
                                "amount": item.cost,
                                "quantity": item.quantity,}
            cartitems.append(v)
            idx += 1
        siteURL = siteroot.absolute_url()
        # having to do some magic with the URL passed to Paypal so their system replaies properly
        returnURL = "%s/register/@@getpaid-thank-you#content" % siteURL
        IPNURL = "%s/%s" % (siteURL, urllib.quote_plus("@@getpaid-paypal-ipnreactor"))
        taxes = order.getTaxCost()
        taxtotal = sum( [ x['value'] for x in taxes ] )
        formvals = {
            "site": _sites[options.server_url],
            "merchant_id": options.merchant_id,
            "cart": ''.join(cartitems),
            "return_url": returnURL,
            "currency": options.currency,
            "IPN_url" : IPNURL,
            "order_id" : order.order_id,
            "store_name": manage_options.store_name,
            "tax_cart": taxtotal,
            }
        return _button_form % formvals
    
    def capture(self, order, price):
        # always returns async - just here to make the processor happy
        return GetPaidInterfaces.keys.results_async

    def authorize( self, order, payment ):
        pass
