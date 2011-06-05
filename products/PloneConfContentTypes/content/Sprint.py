# -*- coding: utf-8 -*-
#
# File: Sprint.py
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

from Products.ATContentTypes.content.event import ATEvent
from Products.ATContentTypes.content.event import ATEventSchema
from Products.PloneConfContentTypes.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Sprint_schema = ATEventSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Sprint(ATEvent):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ISprint)

    meta_type = 'Sprint'
    _at_rename_after_creation = True

    schema = Sprint_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(Sprint, PROJECTNAME)
# end of class Sprint

##code-section module-footer #fill in your manual code here
##/code-section module-footer



