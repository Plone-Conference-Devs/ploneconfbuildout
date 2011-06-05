# -*- coding: utf-8 -*-
#
# File: PloneConfNewsItem.py
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

from Products.ATContentTypes.content.newsitem import ATNewsItem
from Products.ATContentTypes.content.newsitem import ATNewsItemSchema
from Products.PloneConfContentTypes.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

PloneConfNewsItem_schema = ATNewsItemSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class PloneConfNewsItem(ATNewsItem):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPloneConfNewsItem)

    meta_type = 'PloneConfNewsItem'
    _at_rename_after_creation = True

    schema = PloneConfNewsItem_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    def exclude_from_nav(self):
        return True



registerType(PloneConfNewsItem, PROJECTNAME)
# end of class PloneConfNewsItem

##code-section module-footer #fill in your manual code here
##/code-section module-footer



