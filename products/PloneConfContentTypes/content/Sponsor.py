# -*- coding: utf-8 -*-
#
# File: Sponsor.py
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

    StringField(
        name='title',
        widget=StringField._properties['widget'](
            label="Sponsor Name",
            description="Company, organisation or individual's name",
            label_msgid='PloneConfContentTypes_label_title',
            description_msgid='PloneConfContentTypes_help_title',
            i18n_domain='PloneConfContentTypes',
        ),
        required= True,
    ),
    StringField(
        name='contactName',
        widget=StringField._properties['widget'](
            label="Contact Name",
            label_msgid='PloneConfContentTypes_label_contactName',
            i18n_domain='PloneConfContentTypes',
        ),
    ),
    ImageField(
        name='image',
        widget=ImageField._properties['widget'](
            label="Logo",
            description="(if applicable)",
            label_msgid='PloneConfContentTypes_label_image',
            description_msgid='PloneConfContentTypes_help_image',
            i18n_domain='PloneConfContentTypes',
        ),
        storage=AnnotationStorage(),
        sizes={'preview':(200, 200), 'platinum':(260, 500), 'platinumPortlet':(158,500), 'default':(130, 500),},
    ),
    StringField(
        name='website',
        widget=StringField._properties['widget'](
            label="Website Address",
            description="Include http://",
            label_msgid='PloneConfContentTypes_label_website',
            description_msgid='PloneConfContentTypes_help_website',
            i18n_domain='PloneConfContentTypes',
        ),
    ),
    StringField(
        name='email',
        widget=StringField._properties['widget'](
            label="Email address",
            label_msgid='PloneConfContentTypes_label_email',
            i18n_domain='PloneConfContentTypes',
        ),
    ),
    StringField(
        name='sponsorshipLevel',
        default="",
        widget=SelectionWidget(
            label="Level of Sponsorship",
            label_msgid='PloneConfContentTypes_label_sponsorshipLevel',
            i18n_domain='PloneConfContentTypes',
        ),
        required=True,
        vocabulary=[(' ', ' ' ),('platinum','Platinum'),('gold','Gold'),('silver','Silver'),('bronze','Bronze'),('supporting','Supporting'),],
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Sponsor_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Sponsor(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ISponsor)

    meta_type = 'Sponsor'
    _at_rename_after_creation = True

    schema = Sponsor_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    def Title(self):
        return self.title

    def hasImage(self):
        """ Does it have an image? """
        image = self.getImage()
        return image and (getattr(image, 'size', 0) > 0)

    def exclude_from_nav(self):
        return True



registerType(Sponsor, PROJECTNAME)
# end of class Sponsor

##code-section module-footer #fill in your manual code here
##/code-section module-footer



