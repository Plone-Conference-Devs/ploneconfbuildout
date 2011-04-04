# -*- coding: utf-8 -*-
#
# File: PloneConfImage.py
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

from Products.ATContentTypes.content.image import ATImage
from Products.ATContentTypes.content.image import ATImageSchema
from Products.PloneConfContentTypes.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ImageField(
        name='image',
        widget=ImageField._properties['widget'](
            label="Image",
            label_msgid='PloneConfContentTypes_label_image',
            i18n_domain='PloneConfContentTypes',
        ),
        required=True,
        storage=AnnotationStorage(),
        primary=True,
        sizes={'large'   : (768, 768), 'fullwidth' :(520, 520), 'preview' : (400, 400), 'mini'    : (200, 200), 'thumb'   : (128, 128), 'tile'    :  (64, 64), 'icon'    :  (32, 32), 'listing' :  (16, 16), },
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

PloneConfImage_schema = ATImageSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class PloneConfImage(ATImage):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPloneConfImage)

    meta_type = 'PloneConfImage'
    _at_rename_after_creation = True

    schema = PloneConfImage_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods
    # Manually created methods

    def exclude_from_nav(self):
        return True



registerType(PloneConfImage, PROJECTNAME)
# end of class PloneConfImage

##code-section module-footer #fill in your manual code here
##/code-section module-footer



