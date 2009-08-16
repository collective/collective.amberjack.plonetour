from tour2 import go_to_folder
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.amberjack.plonetour')
PMF = MessageFactory('plone')

step_open_display_menu = {'description': _(u"Click the [Display] drop-down menu"),
                      'idStep': 'menu_display',
                      'selector': '',
                      'text': ''}

welcome = go_to_folder.copy()
welcome['title'] = _(u"Change the Folder Display")
welcome['text'] = _(u"A folder is a special content type in Plone because it can contain other content items. The way that those contained items will appear on the screen can be changed using the Display drop-down menu.")

change_in_summary_view = {'url': '/myfolder',
              'xpath': '',
              'xcontent': '',
              'title': _(u"Use summary view"),
              'text': "",
              'steps': (step_open_display_menu,
                        {'description': _(u"Select [Summary] View"),
                      'idStep': 'view_summary',
                      'selector': '',
                      'text': ''}
                        )}

summary_view = {'url': '/myfolder',
                 'xpath': 'body.template-folder_summary_view',
                 'xcontent': 'aj_xpath_exists',
                 'title': _(u"Summary View"),
                 'text' : (u"Up to this point MyFolder has been using the Standard View. Standard view lists each item in the order it happens to be in the folder. Summary View is similar except that each entry is separated by a horizontal line and a Read More . . . link is automatically generated. If an item has an attached thumbnail image (such as a New Item) the image will also appear in the Summary View."),
                 'steps': (step_open_display_menu,
                           {'description': _(u"Select [Tabular] View"),
                          'idStep': 'view_tabular',
                          'selector': '',
                          'text': ''})}

tabular_view = {'url': '/myfolder',
                 'xpath': 'body.template-folder_tabular_view',
                 'xcontent': 'aj_xpath_exists',
                 'title': _(u"Tabular View"),
                 'text' : (u"The Tabular View is similar to what you see in the Contents tab, except that you cannot perform administrative tasks such copy, cut, delete or reorder. The tabular view only displays the Title and Item Type to anonymous site visitors."),
                 'steps': (step_open_display_menu,
                           {'description': _(u"Select [Content Item as Default] View"),
                          'idStep': 'default_page',
                          'selector': '',
                          'text': ''})}

content_item_view = {'url': '/myfolder/select_default_page',
              'xpath': '',
              'xcontent': '',
              'title': _(u"Choose a Default Content Item"),
              'text': _(u"So far you have seen the various ways that a folder in Plone can display its contents. However, in many cases you may wish to choose a single item such as a Page to act as the 'landing page' for the folder. This is common in cases where the folder is intended to be a subsection of the site."),
              'steps': ({'description': _(u"Select [My Page] as the default page for MyFolder."),
                      'idStep': 'radio',
                      'selector': '#my-page',
                      'text': 'checked'},
                      {'description':_(u"Click the [Save] button to finish."),
                       'idStep':'form_save_default_page',
                       'selector':'',
                       'text':''
                       }
                        )}

all_done = {'url': '/myfolder',
                 'xpath': "body.template-document_view",
                 'xcontent': 'aj_xpath_exists',
                 'title': _(u"All done!"),
                 'text': _(u"In this tutorial you have explored some of the ways that a folder can display its contents. On your own, try out the Thumbnail View by uploading several images to a folder. This view is used to create a simple photo gallery."),
                 'steps': ()}

ajTour = {'tourId': 'basic11_using_display_menu',
          'title': _(u'Using the Display Menu'),
          'steps': (welcome,
                    change_in_summary_view,
                    summary_view,
                    tabular_view,
                    content_item_view,
                    all_done,
                   )}

