# -*- coding: utf-8 -*-
#
# File: PloneConfFile.py
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

from Products.ATContentTypes.content.file import ATFile
from Products.ATContentTypes.content.file import ATFileSchema
from Products.PloneConfContentTypes.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

PloneConfFile_schema = ATFileSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class PloneConfFile(ATFile):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPloneConfFile)

    meta_type = 'PloneConfFile'
    _at_rename_after_creation = True

    schema = PloneConfFile_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(PloneConfFile, PROJECTNAME)
# end of class PloneConfFile

##code-section module-footer #fill in your manual code here
##/code-section module-footer



