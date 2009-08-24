from Products.CMFCore.utils import getToolByName


def isFolderCreated(context):
    portal = getToolByName(context, 'portal_url').getPortalObject()
    myfolder = getattr(portal, 'myfolder', None)
    return myfolder is not None

def isNotFolderCreated(context):
    return not isFolderCreated(context)
