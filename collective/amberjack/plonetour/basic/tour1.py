from zope.i18nmessageid import MessageFactory
_ = MessageFactory('collective.amberjack.plonetour')
PMF = MessageFactory('plone')

add_folder = {'url': '/',
           'xpath': '',
           'xcontent': '',
           'title': _(u"Create a new folder"),
           'text': _(u"Folders are one of the most fundamental content types in Plone. You can use a folder to organize your documents much like you already do on your desktop computer. You can also use folders to create new sections of your website."),
           'steps': ({'description': _(u"If you don't want to perform the indicated step yourself, just click the '>>' link and it will be automatically done by your browser."),
                      'idStep': '',
                      'selector': '',
                      'text': ''},
                     {'description': _(u"Click the [Add new...] drop-down menu."),
                      'idStep': 'menu_add-new',
                      'selector': '',
                      'text': ''},
                     {'description': _(u"Select [Folder] from the choices there."),
                      'idStep': 'new_folder',
                      'selector': '',
                      'text': ''})}

fill_out_the_fields = {'url': '/portal_factory/Folder/folder',
              'xpath': '',
              'xcontent': '',
              'title': _(u"Fill out the fields"),
              'text': "",
              'steps': ({'description': _(u"In the [Title] field, type 'MyFolder'."),
                         'idStep': 'form_title',
                         'selector': '',
                         'text': 'MyFolder'},
                        {'description': _(u"In the [Description] field, type 'This folder will be used to contain sample content as I work through each tutorial.'."),
                         'idStep': 'form_description',
                         'selector': '',
                         'text': _("This folder will be used to contain sample content as I work through each tutorial.")},
                        {'description': _(u"Now click the [Save] button at the bottom of the page to save your new folder."),
                         'idStep': 'form_save',
                         'selector': '',
                         'text': ''})}

publish_folder = {'url': '/myfolder',
                 'xpath': '',
                 'xcontent': '',
                 'title': _(u"Publish the folder"),
                 'text' : (u"You have now created a Folder for your Plone website. You should publish your folder so that site visitors can see it."),
                 'steps': ({'description': _(u"Click the [State] drop-down menu."),
                            'idStep': 'menu_state',
                            'selector': '',
                            'text': ''},
                           {'description': _(u"Select [Publish] from the menu."),
                            'idStep': 'content_publish',
                            'selector': '',
                            'text': ''})}

all_done = {'url': '/myfolder',
                 'xpath': "#plone-contentmenu-workflow dt a span.state-published",
                 'xcontent': PMF(u"Published"),
                 'title': _(u"All done!"),
                 'text': _(u"You now have a folder on your Plone website. You will use this folder in the remaining tutorials as a place to put sample content. <strong>Do not delete or rename it</strong> until you are finished with all the tutorials!"),
                 'steps': ()}

ajTour = {'tourId': 'basic01_add_and_publish_a_folder',
          'title': _(u'Add and publish a Folder'),
          'steps': (add_folder,
                    fill_out_the_fields,
                    publish_folder,
                    all_done,
                   )}

