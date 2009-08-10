"""
a tour has this shape:

        {
             'tourId':'example_tour',
             'title': 'Example tour',
             'skinId':'safari',
             'ajsteps': <ajsteps>,
             }

ajsteps has this shape:

                     ({
                      'url':'/',
                      'xpath':'',
                      'xcontent':'',
                      'title':'',
                      'text':'''
                            ''',
                      'steps':({
                                'description': '',
                                'idStep' : '',
                                'selector' : '',
                                'text' : ''
                               },
                               ...
                               ) 
                            
                      },
                      ...
                      )
                      
                      
The set of current tour's steps
 - the description for the user (use [] to <span class="ajHighlight">highlight</span> parts), 
 - the step id, [see collective.amberjack.core.javascript.ajStandardSteps.ajStandardSteps]
 - an optional selector
 - an optional text used by the step

"""
welcome = {
          'url':'/',
          'xpath':'',
          'xcontent':'',
          'title':'Welcome to this screencast about Plone4ArtistsVideo',
          'text':"""
                    Learn about uploading video files, and embedding videos on your Plone site, 
                    that are hosted on popular video sharing sites such as Youtube and Google Video.
                """,
          'steps':({
                    'description': '''Now let's open the [Add New] menu''',
                    'idStep' : 'menu_add-new',
                    'selector' : '',
                    'text' : ''
                   },
                   {
                    'description': '''Create a [new folder]''',
                    'idStep' : 'new_folder',
                    'selector' : '',
                    'text' : ''
                   },) 
          }

add_folder = {
          'url':'/portal_factory/Folder/folder',
          'xpath':'',
          'xcontent':'',
          'title':'create the folder',
          'text':"""
                    Lorem ipsum dolor sit <b>amet</b>, consectetur adipiscing elit. Aenean cursus est in lorem hendrerit varius ut ut tortor. 
                    Mauris pretium lectus quis nibh rhoncus eget iaculis ipsum lobortis.
                """,
          'steps':({
                    'description': '''Set folder [title] to "MyFolder"''',
                    'idStep' : 'form_title',
                    'selector' : '',
                    'text' : 'MyFolder'
                   },
                   {
                    'description': '''Then [save]''',
                    'idStep' : 'form_save',
                    'selector' : '',
                    'text' : ''
                   },) 
                
          }

create_event = {
          'url':'/myfolder/',
          'xpath':'',
          'xcontent':'',
          'title':'add an Event',
          'text':"""
                  Pellentesque varius, metus non venenatis semper, urna mi mattis sapien, ut placerat quam enim nec diam. Integer dictum purus ac lectus tempus pellentesque. 
                  Aliquam eu magna ac mauris ullamcorper egestas non vel augue.
                """,
          'steps':({
                    'description': "Now let's open the [Add New] menu",
                    'idStep' : 'menu_add-new',
                    'selector' : '',
                    'text' : ''
                   },
                   {
                    'description': "And let's create a new [Event]",
                    'idStep' : 'new_event',
                    'selector' : '',
                    'text' : ''
                   },
                   ) 
                
          }

fill_event = {
              'url':'/myfolder/portal_factory/Event',
              'xpath':'',
              'xcontent':'',
              'title':'complete the fields and save it',
              'text':"""
                      Pellentesque varius, metus non venenatis semper, urna mi mattis sapien, ut placerat quam enim nec diam. Integer dictum purus ac lectus tempus pellentesque. 
                      Aliquam eu magna ac mauris ullamcorper egestas non vel augue.
                    """,
              'steps':({
                        'description': "Set Event's [Title] to 'MyEvent'",
                        'idStep' : 'form_title',
                        'selector' : '',
                        'text' : 'MyEvent'
                       },
                       {
                        'description': '''Then [save]''',
                        'idStep' : 'form_save',
                        'selector' : '',
                        'text' : ''
                       },
                       ) 
                    
              }

publish_event = {
              'url': '/myfolder/myevent',
              'xpath':'',
              'xcontent':'',
              'title': "ok, let's publish it",
              'text' : """
                          ...
                      """,
            'steps': ({
                      'description': "Now let's open the [State] menu",
                      'idStep': 'menu_state',
                      'selector':'',
                      'text':''
                      },
                      {
                      'description': "And let's [publish] the new event",
                      'idStep': 'content_publish',
                      'selector':'',
                      'text':''
                      },)
            }



see_the_event = {
              'url':'/myfolder/myevent',
              'xpath':"#plone-contentmenu-workflow dt a span.state-published",
              'xcontent':"",
              'title': 'Done',
              'text': """Great job dude!<br> close the tour now""",
              'steps': ()
           }

ajTour = {
             'tourId':'example_tour',
             'title': 'Example tour',
             'skinId':'safari',
             'ajsteps':(welcome,
                      add_folder,
                      create_event,
                      fill_event,
                      publish_event,
                      see_the_event,
                      )
    
    }
