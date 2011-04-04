# -*- coding: utf-8 -*-

from zope.interface import Interface

##code-section HEAD
##/code-section HEAD

class ISponsor(Interface):
    """Marker interface for .Sponsor.Sponsor
    """

class IPloneConfNewsItem(Interface):
    """Marker interface for .PloneConfNewsItem.PloneConfNewsItem
    """

class IPloneConfNewsItemFolder(Interface):
    """Marker interface for .PloneConfNewsItemFolder.PloneConfNewsItemFolder
    """

class ISprint(Interface):
    """Marker interface for .Sprint.Sprint
    """

class ICourse(Interface):
    """Marker interface for .Course.Course
    """

class IHomepage(Interface):
    """Marker interface for .Homepage.Homepage
    """

class IPloneConfDocument(Interface):
    """Marker interface for .PloneConfDocument.PloneConfDocument
    """

class IPloneConfFolder(Interface):
    """Marker interface for .PloneConfFolder.PloneConfFolder
    """

class IPloneConfImage(Interface):
    """Marker interface for .PloneConfImage.PloneConfImage
    """

class IPloneConfFile(Interface):
    """Marker interface for .PloneConfFile.PloneConfFile
    """

##code-section FOOT
##/code-section FOOT