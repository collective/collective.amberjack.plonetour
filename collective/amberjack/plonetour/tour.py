"""
A tour has this shape:

    {'tourId': 'example_tour',
     'title': _(u"Example tour"),
     'skinId': 'safari',
     'ajsteps': <ajsteps>}

<ajsteps> has this shape:

    ({'url': '/',
      'xpath': '',
      'xcontent': '',
      'title': _(u"Some title"),
      'text': _(u"Some text"),
      'steps': ({'description': _(u"Some description"),
                 'idStep': '',
                 'selector': '',
                 'text': ''},
                ...
               )       
     },
     ...
    )
                      
                      
The set of current tour's steps:

 - the description for the user (use [] to <span class="ajHighlight">highlight</span> parts), 
 - the step id, [see collective.amberjack.core.javascript.ajStandardSteps.ajStandardSteps]
 - an optional selector
 - an optional text used by the step

"""

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('collective.amberjack.plonetour')
PMF = MessageFactory('plone')

welcome = {'url': '/',
           'xpath': '',
           'xcontent': '',
           'title': _(u"Welcome to this screencast about Plone4ArtistsVideo"),
           'text': _(u"Learn about uploading video files, and embedding videos on your Plone site, that are hosted on popular video sharing sites such as Youtube and Google Video."),
           'steps': ({'description': _(u"Now let's open the [Add new...] menu"),
                      'idStep': 'menu_add-new',
                      'selector': '',
                      'text': ''},
                     {'description': _(u"Create a new [Folder]"),
                      'idStep': 'new_folder',
                      'selector': '',
                      'text': ''})}

add_folder = {'url': '/portal_factory/Folder/folder',
              'xpath': '',
              'xcontent': '',
              'title': _(u"create the folder"),
              'text': """Lorem ipsum dolor sit <b>amet</b>, consectetur adipiscing elit.
                         Aenean cursus est in lorem hendrerit varius ut ut tortor.
                         Mauris pretium lectus quis nibh rhoncus eget iaculis ipsum lobortis.""",
              'steps': ({'description': _(u"Set folder [Title] to 'MyFolder'"),
                         'idStep': 'form_title',
                         'selector': '',
                         'text': 'MyFolder'},
                        {'description': _(u"Then [save]"),
                         'idStep': 'form_save',
                         'selector': '',
                         'text': ''})}

create_event = {'url': '/myfolder/',
                'xpath': '',
                'xcontent': '',
                'title': _(u"add an Event"),
                'text': """Pellentesque varius, metus non venenatis semper, urna mi mattis sapien,
                           ut placerat quam enim nec diam. Integer dictum purus ac lectus tempus pellentesque. 
                           Aliquam eu magna ac mauris ullamcorper egestas non vel augue.""",
                'steps': ({'description': _(u"Now let's open the [Add new...] menu"),
                           'idStep': 'menu_add-new',
                           'selector': '',
                           'text': ''},
                          {'description': _(u"And let's create a new [Event]"),
                           'idStep': 'new_event',
                           'selector': '',
                           'text': ''})}

fill_event = {'url': '/myfolder/portal_factory/Event',
              'xpath': '',
              'xcontent': '',
              'title': _(u"complete the fields and save it"),
              'text': """Pellentesque varius, metus non venenatis semper, urna mi mattis sapien,
                         ut placerat quam enim nec diam. Integer dictum purus ac lectus tempus pellentesque. 
                         Aliquam eu magna ac mauris ullamcorper egestas non vel augue.""",
              'steps': ({'description': _(u"Set Event's [Title] to 'MyEvent'"),
                         'idStep': 'form_title',
                         'selector': '',
                         'text': 'MyEvent'},
                        {'description': _(u"Then [save]"),
                         'idStep': 'form_save',
                         'selector': '',
                         'text': ''})}

publish_event = {'url': '/myfolder/myevent',
                 'xpath': '',
                 'xcontent': '',
                 'title': _(u"ok, let's publish it"),
                 'text' : """...""",
                 'steps': ({'description': _(u"Now let's open the [State] menu"),
                            'idStep': 'menu_state',
                            'selector': '',
                            'text': ''},
                           {'description': _(u"And let's [publish] the new event"),
                            'idStep': 'content_publish',
                            'selector': '',
                            'text': ''})}

see_the_event = {'url': '/myfolder/myevent',
                 'xpath': "#plone-contentmenu-workflow dt a span.state-published",
                 'xcontent': PMF(u"Published"),
                 'title': _(u"Done"),
                 'text': _(u"Great job dude! Close the tour now"),
                 'steps': ()}

ajTour = {'tourId': 'example_tour',
          'title': 'Example tour',
          'skinId': 'safari',
          'ajsteps': (welcome,
                      add_folder,
                      create_event,
                      fill_event,
                      publish_event,
                      see_the_event,
                     )}

