#from p4a.subtyper import engine
#from p4a.subtyper import interfaces
from zope.component import getUtility 

def setupOutOfTheBox_ploneTour(context):
    #BBB need to fix this!!
    """if context.readDataFile('marker_p4aTour.txt') is None:
            return
    """
    portal = context.getSite()
    folder = createObject('newfolder', 'Folder', portal)
    #if folder:
        #subtyper = getUtility(interfaces.ISubtyper)
        #subtyper.change_type(folder, u'p4a.video.FolderVideoContainer')    
        #link = createObject('a video from youtube', 'Link', folder)
        #if link:
            #link.setRemoteUrl('http://www.youtube.com/watch?v=FfGmTzabFM8')
            #subtyper.change_type(link, 'p4a.video.VideoLink')
        

def createObject(title, type_name, context):
    id_ = normalize(title)

    if not id_ in context.objectIds():
        context.invokeFactory(id=id_, type_name=type_name)
        object = context[id_]
        object.setTitle(title)
        return object
    
def normalize(u):
    return u.lower().replace(' ', '-')