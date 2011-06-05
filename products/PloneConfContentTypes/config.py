# -*- coding: utf-8 -*-
#
# File: PloneConfContentTypes.py
#
# Copyright (c) 2010 by []
# Generator: ArchGenXML Version 2.4.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


# Product configuration.
#
# The contents of this module will be imported into __init__.py, the
# workflow configuration and every content type module.
#
# If you wish to perform custom configuration, you may put a file
# AppConfig.py in your product's root directory. The items in there
# will be included (by importing) in this file if found.

from Products.CMFCore.permissions import setDefaultRoles
##code-section config-head #fill in your manual code here
##/code-section config-head


PROJECTNAME = "PloneConfContentTypes"

# Permissions
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner', 'Contributor'))
ADD_CONTENT_PERMISSIONS = {
    'Sponsor': 'PloneConfContentTypes: Add Sponsor',
    'PloneConfNewsItem': 'PloneConfContentTypes: Add PloneConfNewsItem',
    'PloneConfNewsItemFolder': 'PloneConfContentTypes: Add PloneConfNewsItemFolder',
    'Sprint': 'PloneConfContentTypes: Add Sprint',
    'Course': 'PloneConfContentTypes: Add Course',
    'Homepage': 'PloneConfContentTypes: Add Homepage',
    'PloneConfDocument': 'PloneConfContentTypes: Add PloneConfDocument',
    'PloneConfFolder': 'PloneConfContentTypes: Add PloneConfFolder',
    'PloneConfImage': 'PloneConfContentTypes: Add PloneConfImage',
    'PloneConfFile': 'PloneConfContentTypes: Add PloneConfFile',
}

setDefaultRoles('PloneConfContentTypes: Add Sponsor', ('Manager','Owner'))
setDefaultRoles('PloneConfContentTypes: Add PloneConfNewsItem', ('Manager','Owner'))
setDefaultRoles('PloneConfContentTypes: Add PloneConfNewsItemFolder', ('Manager','Owner'))
setDefaultRoles('PloneConfContentTypes: Add Sprint', ('Manager','Owner'))
setDefaultRoles('PloneConfContentTypes: Add Course', ('Manager','Owner'))
setDefaultRoles('PloneConfContentTypes: Add Homepage', ('Manager','Owner'))
setDefaultRoles('PloneConfContentTypes: Add PloneConfDocument', ('Manager','Owner'))
setDefaultRoles('PloneConfContentTypes: Add PloneConfFolder', ('Manager','Owner'))
setDefaultRoles('PloneConfContentTypes: Add PloneConfImage', ('Manager','Owner'))
setDefaultRoles('PloneConfContentTypes: Add PloneConfFile', ('Manager','Owner'))

product_globals = globals()

# Dependencies of Products to be installed by quick-installer
# override in custom configuration
DEPENDENCIES = []

# Dependend products - not quick-installed - used in testcase
# override in custom configuration
PRODUCT_DEPENDENCIES = []

##code-section config-bottom #fill in your manual code here
##/code-section config-bottom


# Load custom configuration not managed by archgenxml
try:
    from Products.PloneConfContentTypes.AppConfig import *
except ImportError:
    pass
