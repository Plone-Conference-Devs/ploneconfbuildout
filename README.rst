Introduction
============
This is in progress. Tread lightly and carry a big stick!

Setup the Dev Environment
-------------------------
The usual really. None of the production configs have been 
tested yet so if you test them and they work please update 
this note :)

For development::

 > python bootstrap.py
 > ./bin/buildout
 > ./bin/local fg
 
Note that the default port is 12801 instead of 8080. 

Before the Sprint
-----------------
 * Identify sponsorship levels
 * Solidify ticket prices and discounts
 * Set up authorize.net account

Major TODO's
------------
 * Integrate Brown Paper Tickets. Look at netsight.registration and see if
   we want to reuse that.
 * Handle sponsorship integration with authorize.net account. Would be nice if 
   the PF could reuse this on their site. Would be especially nice if we could 
   collect money and have them automatically upload their own logo. Is there a 
   sponsors product that could do this? That would be useful on several plone 
   infra sites IMHP/
 * Add the following pages by default and load with generic content for modifying 
   later (so all the links works):
   
   * Event: about the event, the schedule, sprint info, etc...
   * The Area: on the venue, getting to sf, etc
   * Party Details
   * Sponsor: what the levels are and how to contact

Notes on Brown Paper Tickets integration
----------------------------------------

I (davisagli) started a package, getpaid.brownpapertickets, to serve as a Getpaid
payment processor using the BPT API.

This is probably the way we want to go (vs. having people purchase tickets via
BPT's UI) so that we can collect and store our own info. BPT supports custom
fields but its API does not seem to.

The registration form in netsight.conferenceregistration will need to be updated
to retrieve price info and ids from BPT so it can store the selected price_id
in the product_code of the cart line item.

Currently the integration is not working yet. I'm getting "Not enough tickets
available" as the error code when it tries to add tickets to the cart. I presume
that's because our event hasn't been approved yet.

Steps to set up for testing:

1. Install "Plone Conference 2010 Registration System" and PloneGetPaid.
2. Go to the GetPaid control panel > Payment Options and set the Payment Processor
   to "Brown Paper Tickets"
3. Go to the GetPaid control panel > Payment Processor Settings and enter the
   Developer ID (found when logged into the BPT account and super-secret) and
   make sure test mode is on.
4. Add a folder to the site called 'registrations'. Add a folder inside it called
   'attendees'.
5. Go to the registrations folder in the ZMI, click on the Interfaces tab and
   enable the IRegistrationFolder marker interface.
6. Go to /registrations/@@registration and go through the checkout process.
   Use a dummy credit card #, 1234567890000000 will work.
