"""
"""

from getpaid.core.options import PersistentOptions
import interfaces

PaypalStandardOptions = PersistentOptions.wire("PaypalStandardOptions",
                                               "getpaid.paypal",
                                               interfaces.IPaypalStandardOptions )

