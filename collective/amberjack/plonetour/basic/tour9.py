from tour2 import go_to_folder
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('collective.amberjack.plonetour')
PMF = MessageFactory('plone')

welcome = go_to_folder.copy()
welcome['title'] = _(u"Create a File")
welcome['text'] = _(u"A File in Plone is any binary file such as a PDF, DOC, XLS, PPT, RTF, or other file type that you wish to upload to your site. You can also link to a file to allow your site visitors the chance to download the file.")

add_file = {
    'url': '/myfolder',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Add a new Image to MyFolder"),
    'text': _(u""),
    'steps': ({'description': _(u"Click the [Add New...] drop-down menu and select Image from the menu."),
               'idStep': 'menu_add-new',
               'selector': '',
               'text': ''},
               {'description': _(u"Select [File] from the menu."),
               'idStep': 'new_file',
               'selector': '',
               'text': ''},
             )}


choose_file = {
    'url': '/myfolder/portal_factory/File',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Choose a file"),
    'text': "Simply provide a title, description, and select the file you wish to upload.",
    'steps': ({'description': _(u"Provide a [Title]."),
               'idStep': 'form_title',
               'selector': '',
               'text': 'My File'},
               {'description': _(u"Provide a [Description]. The description will appear in site searches and in summary listings of files on your site."),
               'idStep': 'form_description',
               'selector': '',
               'text': _(u'A description for this file')},
               {'description': _(u"Click the [Browse] button."),
               'idStep': 'file_file',
               'selector': '',
               'text': ''},
               {'description': _(u"Select a file from your desktop computer."),
               'idStep': '',
               'selector': '',
               'text': ''},
               {'description': _(u"Click [Save] to complete the upload."),
               'idStep': 'form_save',
               'selector': '',
               'text': ''},     
             )}

link_to_file = {
    'url': '/myfolder',
    'xpath': 'a[@href="AJ_ROOT/myfolder/my-file"]',
    'xcontent': 'aj_xpath_exists',
    'title': _(u"Link to the File"),
    'text': _(u"You now have a file on your Plone website. You should now create a link to the file from a page to allow a site visitor to download the file. Otherwise, a site visitor would have to know the web address for the file or happen to search for it."),
    'steps': ({'description': _(u"Navigate to [My Page]"),
               'idStep': 'link',
               'selector': 'a[@href="AJ_ROOT/myfolder/my-page"]',
               'text': ''},
             )}

edit_page = {
    'url': '/myfolder/my-page',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Edit an existing page"),
    'text': _(u""),
    'steps': ({'description': _(u"Click the [Edit] tab."),
               'idStep': 'contentview_edit',
               'selector': '',
               'text': ''},
               )}

insert_internal_link = {
    'url': '/myfolder/my-page/edit',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Insert an internal link"),
    'text': _(u"When linking to a file, you should indicate that the link will begin the download of a file and you should indicate the file type and size in the link text as well. For example you might say: Download this report [PDF 1.2 Mb]."),
    'steps': ({'description': _(u"Type some link text in the [Body Text] field of the page (i.e. Download this report)."),
               'idStep': 'text_area',
               'selector': '',
               'text': 'Download this report [PDF 1.2 Mb]'},
               {'description': _(u"Now highlight the link text and click the [Internal Link] icon in the editor toolbar (it looks like a piece of chain link)."),
               'idStep': 'button_internal_link',
               'selector': '',
               'text': ''},
               {'description': _(u"Use the [pop-up window] to browse to the location of the file you just uploaded."),
               'idStep': '',
               'selector': '',
               'text': ''},
               {'description': _(u"Select the file by [clicking the radio button] next to it."),
               'idStep': '',
               'selector': '',
               'text': ''},
               {'description': _(u"Click [OK] to create the hyperlink."),
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
    'xpath': '#content a.internal-link',
    'xcontent': 'aj_xpath_exists',
    'title': _(u"All done!"),
    'text': _(u"You now have a linked file on your Plone website. Try clicking the link to see what the download process looks like. Note that the browser settings of each site visitor will determine whether the file opens in an application or if the Save As dialog box appears. You cannot control this behavior from within Plone."),
    'steps': ()}

ajTour = {'tourId': 'basic09_upload_and_link_to_a_file',
          'title': _(u"Upload and link to a File"),
          'steps': (welcome,
                    add_file,
                    choose_file,
                    link_to_file,
                    edit_page,
                    insert_internal_link,
                    all_done,
                   )}

