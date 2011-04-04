import decimal
from zope.formlib import form
from zope.interface import implements

from zope import schema, component
from Products.CMFCore.utils import getToolByName

from getpaid.core.interfaces import ITaxUtility

from getpaid.vatplus import getpaidvatplusMessageFactory as _

from Products.PloneGetPaid.browser.base import StockFormViewlet


class TaxUtility(object):
    implements(ITaxUtility)

    def getCost(self, order):
        """Calculate VAT at 14% on the subtotal and any shipping costs"""
        return float(order.getSubTotalPrice() + order.getShippingCost()) * self.tax_rate

    def getTaxes(self, order):
        return [{'value' : self.getCost(order), 'name' : self.tax_name}]


    def getTaxOnSum(self, sum):
        """Return the VAT value of a price, rounded to the nearest cent"""
        return float('%.2f' % (sum * self.tax_rate))

    @property
    def tax_rate(self):
        return 0.175

    @property
    def tax_name(self):
        return _(u"VAT")


class VATConfig( StockFormViewlet ):

    form_fields = form.Fields(
        schema.TextLine(__name__='vatnumber', title=u"VAT Number"),
        )

    form_name = "VAT Number"
    form_description = "If you are in Europe and have a VAT number, enter it below and we will remove VAT from the invoice"
    
    @form.action(_("Update VAT"), name='update-vat')
    def handle_update_vat( self, action, data ):

        utility = component.getUtility( interfaces.IShoppingCartUtility )
        cart = utility.get(self.context, create=True)

        cart.vatnumber = data['vatnumber']

        # Go back to the registration form
        portal = getToolByName( self.context, 'portal_url').getPortalObject()
        url = portal.absolute_url() + '/@@getpaid-cart'
        return self.request.RESPONSE.redirect( url )
