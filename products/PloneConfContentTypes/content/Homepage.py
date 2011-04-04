# -*- coding: utf-8 -*-
#
# File: Homepage.py
#
# Copyright (c) 2010 by []
# Generator: ArchGenXML Version 2.4.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.PloneConfContentTypes.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    LinesField(
        name='reasonsToCome',
        widget=LinesField._properties['widget'](
            label="Reasons to Come",
            description="One per line.",
            label_msgid='PloneConfContentTypes_label_reasonsToCome',
            description_msgid='PloneConfContentTypes_help_reasonsToCome',
            i18n_domain='PloneConfContentTypes',
        ),
    ),
    IntegerField(
        name='ticketPrice',
        widget=IntegerField._properties['widget'](
            label="Ticket Price",
            description="In pounds, excluding VAT.",
            label_msgid='PloneConfContentTypes_label_ticketPrice',
            description_msgid='PloneConfContentTypes_help_ticketPrice',
            i18n_domain='PloneConfContentTypes',
        ),
    ),
    IntegerField(
        name='earlybirdPrice',
        widget=IntegerField._properties['widget'](
            label="Earlybird Price",
            description="In pounds, excluding VAT.",
            label_msgid='PloneConfContentTypes_label_earlybirdPrice',
            description_msgid='PloneConfContentTypes_help_earlybirdPrice',
            i18n_domain='PloneConfContentTypes',
        ),
    ),
    DateTimeField(
        name='earlybirdCutOff',
        widget=DateTimeField._properties['widget'](
            label="Earlybird Cut-off date.",
            label_msgid='PloneConfContentTypes_label_earlybirdCutOff',
            i18n_domain='PloneConfContentTypes',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Homepage_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Homepage(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IHomepage)

    meta_type = 'Homepage'
    _at_rename_after_creation = True

    schema = Homepage_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Homepage, PROJECTNAME)
# end of class Homepage

##code-section module-footer #fill in your manual code here
##/code-section module-footer



