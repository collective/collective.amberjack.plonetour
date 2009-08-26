from tour2 import go_to_folder
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('collective.amberjack.plonetour')
PMF = MessageFactory('plone')


welcome = go_to_folder.copy()
welcome['title'] = _(u"Insert image on a page")
welcome['text'] = _(u"In this tutorial, you will revisit a page that you already created and learn how insert an image into that page.")

go_to_page = {
    'url': '/myfolder',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Open 'My Page'"),
    'text': _(u""),
    'steps': ({'description': _(u"Navigate to [My Page] that you created from the previous tutorial."),
               'idStep': 'link',
               'selector': 'a[@href="AJ_ROOT/myfolder/my-page"]',
               'text': ''},
               )}

edit_page = {
    'url': '/myfolder/my-page',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Edit 'My Page'"),
    'text': _(u""),
    'steps': ({'description': _(u"Click the [Edit] tab to begin editing."),
               'idStep': 'contentview_edit',
               'selector': '',
               'text': ''},
               )}

insert_image = {
    'url': '/myfolder/my-page/edit',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Insert an Image"),
    'text': "Position your cursor in the [Body Text] field where you'd like to insert the image. Find or write a paragraph of text and place the cursor to the left of the first character in the paragraph.",
    'steps': ({'description': _(u"Now click the [Insert Image] icon in the editor toolbar (it looks like a tree)."),
               'idStep': 'button_insert_image',
               'selector': '',
               'text': ''},
               {'description': _(u"A pop-up window should appear. [Browse] to the location of an image you would like to insert. You should have at least one image already in MyFolder from a previous tutorial."),
               'idStep': '',
               'selector': '',
               'text': ''},
               {'description': _(u"Select the image by [clicking the radio button] next to it."),
               'idStep': '',
               'selector': '',
               'text': ''},
               {'description': _(u"Notice in the right-hand column of the pop-up window that a preview of the image you have selected appears."),
               'idStep': '',
               'selector': '',
               'text': ''},
               {'description': _(u"Choose [Left] alignment and a [Size] from the size menu. You can leave the [Text Equivalent] field as-is, or change the text if you wish. This is the 'alt' text for the image which aids in site accessibility, search, and indexing."),
               'idStep': 'image_align_left',
               'selector': '',
               'text': ''},
               {'description': _(u"Click [OK] to complete the image insert."),
               'idStep': 'button_dialog_ok',
               'selector': '',
               'text': ''},
               {'description': _(u"Click [Save] to finish."),
               'idStep': 'form_save',
               'selector': '',
               'text': ''},
              
             )}

all_done = {
    'url': '/myfolder/my-page',
    'xpath': '#content img',
    'xcontent': 'aj_xpath_exists',
    'title': _(u"All done!"),
    'text': _(u"You have now successfully inserted an image onto a page. You can edit the page again and insert more images, move existing images around, or change their alignment."),
    'steps': ()}

ajTour = {'tourId': 'basic08_insert_image_on_a_page',
          'title': _(u"Insert image on a page"),
          'steps': (welcome,
                    go_to_page,
                    edit_page,
                    insert_image,
                    all_done,
                   )}
