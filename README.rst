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