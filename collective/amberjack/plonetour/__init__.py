"""
A tour has this shape:

    {'tourId': 'example_tour',
     'title': _(u"Example tour"),
     'steps': <steps>}

<steps> has this shape:

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
