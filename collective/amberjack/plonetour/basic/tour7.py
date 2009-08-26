from tour2 import go_to_folder
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('collective.amberjack.plonetour')
PMF = MessageFactory('plone')

welcome = go_to_folder.copy()
welcome['title'] = _(u"Add a new Image to MyFolder")
welcome['text'] = _(u"Before you can place an image on a page in Plone, you must first upload your image to the site. Be sure that you have properly prepared your image for web publishing. In short, this means that you should compress your image file, use only GIF, JPG, or PNG file formats and crop your image to fit well on the page, and resize it to reduce the upload time if needed.")


add_image = {
    'url': '/myfolder',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Add a new Image to MyFolder"),
    'text': _(u""),
    'steps': ({'description': _(u"Click the [Add New...] drop-down menu and select Image from the menu."),
               'idStep': 'menu_add-new',
               'selector': '',
               'text': ''},
               {'description': _(u"Select [Image] from the menu."),
               'idStep': 'new_image',
               'selector': '',
               'text': ''},
             )}

fill_out_fields = {
    'url': '/myfolder/portal_factory/Image',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Fill out the fields"),
    'text': "Images have three fields you need to fill out. Title, Description, and Browse to choose the file itself.",
    'steps': ({'description': _(u"Provide a [Title] for your Image. It is best if you use the file name of your image as the title, including the file extension (i.e. myphoto.jpg)"),
               'idStep': 'image_title',
               'selector': '',
               'text': 'My Photo'},
               {'description': _(u"Provide a [Description] for your Image."),
               'idStep': 'image_description',
               'selector': '',
               'text': _(u'image description')},
               {'description': _(u"Click the [Browse] button and find the image file you want to upload on your computer's filesystem."),
               'idStep': 'image_file',
               'selector': '',
               'text': ''},
               {'description': _(u"Click [Save] to complete the upload."),
               'idStep': 'form_save',
               'selector': '',
               'text': ''},
             )}

all_done = {
    'url': '/myfolder/XXX',
    'xpath': '',
    'xcontent': '',
    'title': _(u"All done!"),
    'text': _(u"Now that you have uploaded an image to Plone, you can insert the image onto a page. The next tutorial will explain how to insert images."),
    'steps': ()}

ajTour = {'tourId': 'basic07_upload_an_image',
          'title': _(u"Upload an image"),
          'steps': (welcome,
                    add_image,
                    fill_out_fields,
                    all_done,
                   )}

