# -*- coding: utf-8 -*-
#
# File: PloneConfFolder.py
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

from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content.folder import ATFolderSchema
from Products.PloneConfContentTypes.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

PloneConfFolder_schema = ATFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class PloneConfFolder(ATFolder):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPloneConfFolder)

    meta_type = 'PloneConfFolder'
    _at_rename_after_creation = True

    schema = PloneConfFolder_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    def getCustomNavQuery(self):
        return {'is_default_page': [True, False, None, ],}
    


registerType(PloneConfFolder, PROJECTNAME)
# end of class PloneConfFolder

##code-section module-footer #fill in your manual code here
##/code-section module-footer



