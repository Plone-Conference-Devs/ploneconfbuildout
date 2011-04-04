This package provides a payment processor for PayPal_ that can be plugged into the
`GetPaid for Plone framework`_.

.. _PayPal: https://www.paypal.com
.. _`GetPaid for Plone framework`: http://www.plonegetpaid.com/

Installation
============

Add `getpaid.paypal` to your instance eggs and don't forget
the zcml slug (including overrides)::

    eggs =
        getpaid.paypal

    zcml =
        getpaid.paypal
        getpaid.paypal-overrides


Configuration
=============

You will need to set this as your payment processor in the getpaid admin
interface (Payment Options)

Last step is to enter your paypal account info in Payment Processor
Settings.

See https://developer.paypal.com/ for information how to setup a paypal testing account.

Enjoy!
