from tour2 import go_to_folder
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('collective.amberjack.plonetour')
PMF = MessageFactory('plone')

welcome = go_to_folder.copy()
welcome['title'] = _(u"The Contents tab")
welcome['text'] = _(u"So far you've mostly been working with the Edit tab. Now it's time to take a look at the Contents tab and what it can do. The Contents tab lets you browse the filesystem of your website and perform administrative tasks such as: reorder content, delete content, copy, cut, and paste content items.")

edit_page = {
    'url': '/myfolder',
    'xpath': '',
    'xcontent': '',
    'title': _(u"The Contents tab"),
    'text': _(u""),
    'steps': ({'description': _(u"Click on the [Contents] tab."),
               'idStep': 'contentview_content',
               'selector': '',
               'text': ''},
               )}

features_contents_tab = {
    'url': '/myfolder/folder_contents',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Features of the Contents tab"),
    'text': _(u"All of the items you have been creating for these tutorials so far are listed now in the Contents view. You can see information about each item such as the Title, Size, Date Modified, and Publishing State."),
    'steps': ({'description': _(u"Also notice the buttons along the bottom of the Contents view: Copy, Cut, Rename, Delete, and Change State. By using the checkboxes next to each content item you can apply any of these changes to those checked items."),
               'idStep': 'link',
               'selector': '',
               'text': ''},
             )}

reordering_content = {
    'url': '/myfolder/folder_contents',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Reordering content"),
    'text': _(u"You may wish to change the order of contents within a folder for various reasons. One of the most common reasons is to change the order that items list in the Navigation portlet or folder summary views."),
    'steps': ({'description': _(u"Position your mouse pointer over one of the items in the Order column. Notice that your pointer is now a four-way arrow."),
               'idStep': '',
               'selector': '',
               'text': ''},
               {'description': _(u"Click-and-drag the item to the top of the Contents listing. The item is now moved - you do not need to save the change in any way."),
               'idStep': '',
               'selector': '',
               'text': ''},
             )}
copy_content = {
    'url': '/myfolder/folder_contents',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Copy content"),
    'text': _(u"You may wish to make copies of a content item for various reasons. You can paste a copied item into any location on the site."),
    'steps': ({'description': _(u"[Check the box] next to My Page in the contents listing."),
               'idStep': 'checkbox',
               'selector': '#cb_my-page',
               'text': 'checked'},
               {'description': _(u"Click the [Copy] button at the bottom of the page."),
               'idStep': 'folder_copy',
               'selector': '',
               'text': ''},
               )}
               
paste_content = {
    'url': '/myfolder/folder_contents',
    'xpath': 'dl.portalMessage dd',
    'xcontent': PMF('1 item(s) copied.'),
    'title': _(u"Paste content"),
    'text': _(u"XXX You may wish to make copies of a content item for various reasons. You can paste a copied item into any location on the site."),
    'steps': ({'description': _(u"Notice that a Paste button now appears. Click [Paste] to create a copy of My Page."),
               'idStep': 'folder_paste',
               'selector': '',
               'text': ''},
               )}

all_done = {
    'url': '/myfolder/folder_contents',
    'xpath': 'dl.portalMessage dd',
    'xcontent': PMF('Item(s) pasted.'),
    'title': _(u"All done!"),
    'text': _(u"You now have two copies of the same page in your folder.<br />You can cut-and-paste and also delete items in a folder by checking the boxes next to the items you wish to alter."),
    'steps': (
               {'description': _(u"You now have two copies of the same page in your folder."),
               'idStep': '',
               'selector': '',
               'text': ''},
             )}

ajTour = {'tourId': 'basic10_using_the_contents_tab',
          'title': _(u"Using the Contents tab"),
          'steps': (welcome,
                    edit_page,
                    features_contents_tab,
                    reordering_content,
                    copy_content,
                    paste_content,
                    all_done,
                   )}
