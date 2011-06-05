# -*- coding: utf-8 -*-
#
# File: PloneConfDocument.py
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

from Products.ATContentTypes.content.document import ATDocument
from Products.ATContentTypes.content.document import ATDocumentSchema
from Products.PloneConfContentTypes.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

PloneConfDocument_schema = ATDocumentSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class PloneConfDocument(ATDocument):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPloneConfDocument)

    meta_type = 'PloneConfDocument'
    _at_rename_after_creation = True

    schema = PloneConfDocument_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(PloneConfDocument, PROJECTNAME)
# end of class PloneConfDocument

##code-section module-footer #fill in your manual code here
##/code-section module-footer



