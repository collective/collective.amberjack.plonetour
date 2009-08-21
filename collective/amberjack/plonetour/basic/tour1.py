from zope.i18nmessageid import MessageFactory
_ = MessageFactory('collective.amberjack.plonetour')
PMF = MessageFactory('plone')

add_folder = {'url': u'/',
           'xpath': u'',
           'xcontent': u'',
           'title': _(u"Create a new folder"),
           'text': _(u"Folders are one of the most fundamental content types in Plone. You can use a folder to organize your documents much like you already do on your desktop computer. You can also use folders to create new sections of your website."),
           'steps': ({'description': _(u"If you don't want to perform the indicated step yourself, just click the '>>' link and it will be automatically done by your browser."),
                      'idStep': '',
                      'selector': '',
                      'text': ''},
                     {'description': _(u"Click the [Add new...] drop-down menu."),
                      'idStep': u'menu_add-new',
                      'selector': u'',
                      'text': u''},
                     {'description': _(u"Select [Folder] from the choices there."),
                      'idStep': u'new_folder',
                      'selector': u'',
                      'text': u''})}

fill_out_the_fields = {'url': u'/portal_factory/Folder/folder',
              'xpath': u'',
              'xcontent': u'',
              'title': _(u"Fill out the fields"),
              'text': u'',
              'steps': ({'description': _(u"In the [Title] field, type 'MyFolder'."),
                         'idStep': u'form_title',
                         'selector': u'',
                         'text': u'MyFolder'},
                        {'description': _(u"In the [Description] field, type 'This folder will be used to contain sample content as I work through each tutorial.'."),
                         'idStep': u'form_description',
                         'selector': u'',
                         'text': _("This folder will be used to contain sample content as I work through each tutorial.")},
                        {'description': _(u"Now click the [Save] button at the bottom of the page to save your new folder."),
                         'idStep': u'form_save',
                         'selector': u'',
                         'text': u''})}

publish_folder = {'url': u'/myfolder',
                 'xpath': u'',
                 'xcontent': u'',
                 'title': _(u"Publish the folder"),
                 'text' : (u"You have now created a Folder for your Plone website. You should publish your folder so that site visitors can see it."),
                 'steps': ({'description': _(u"Click the [State] drop-down menu."),
                            'idStep': u'menu_state',
                            'selector': u'',
                            'text': u''},
                           {'description': _(u"Select [Publish] from the menu."),
                            'idStep': u'content_publish',
                            'selector': u'',
                            'text': u''})}

all_done = {'url': u'/myfolder',
                 'xpath': u"#plone-contentmenu-workflow dt a span.state-published",
                 'xcontent': PMF(u"Published"),
                 'title': _(u"All done!"),
                 'text': _(u"You now have a folder on your Plone website. You will use this folder in the remaining tutorials as a place to put sample content. <strong>Do not delete or rename it</strong> until you are finished with all the tutorials!"),
                 'steps': ()}

ajTour = {'tourId': u'basic01_add_and_publish_a_folder',
          'title': _(u'Add and publish a Folder'),
          'steps': (add_folder,
                    fill_out_the_fields,
                    publish_folder,
                    all_done,
                   )}

