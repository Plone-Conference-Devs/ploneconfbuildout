"""
"""

from getpaid.core import interfaces
from zope import schema
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('getpaid.paypal')

# generate a Zope 3 vocabulary from a sequence of tuples, suitable for use in a drop-down menu
def _vocabulary(*terms):
    return SimpleVocabulary([SimpleTerm(token, token, title)
                             for token, title in terms])


class IPaypalStandardProcessor( interfaces.IPaymentProcessor ):
    """
    Paypal Standard Processor
    """

class IPaypalStandardOptions( interfaces.IPaymentProcessorOptions ):
    """
    Paypal Standard Options
    """
    server_url = schema.Choice(
        title = _(u"Paypal Website Payments Server"),
        values = ( "Sandbox", "Production" ),
        )

    merchant_id = schema.ASCIILine( title = _(u"Paypal Id"))

    currency = schema.Choice(
        title = _(u"Currency"),
        vocabulary = _vocabulary(
            ('AUD', u'Australian Dollar'),
            ('CAD', u'Canadian Dollar'),
            ('CZK', u'Czech Koruna'),
            ('DKK', u'Danish Krone'),
            ('EUR', u'Euro'),
            ('HKD', u'Hong Kong Dollar'),
            ('HUF', u'Hungarian Forint'),
            ('ILS', u'Israeli New Sheqel'),
            ('JPY', u'Japanese Yen'),
            ('MXN', u'Mexican Peso'),
            ('NOK', u'Norwegian Krone'),
            ('NZD', u'New Zealand Dollar'),
            ('PLN', u'Polish Zloty'),
            ('GBP', u'Pound Sterling'),
            ('SGD', u'Singapore Dollar'),
            ('SEK', u'Swedish Krona'),
            ('CHF', u'Swiss Franc'),
            ('USD', u'U.S. Dollar'),
            )
        )
