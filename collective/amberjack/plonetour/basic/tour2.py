from zope.i18nmessageid import MessageFactory
_ = MessageFactory('collective.amberjack.plonetour')
PMF = MessageFactory('plone')

go_to_folder = {
    'url': '/',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Add and publish a Page"),
    'text': _(u"In this tutorial, you'll create a new Page and publish it on your Plone-powered website."),
    'steps': ({'description': _(u"Navigate to the folder called [MyFolder] that you created in a previous tutorial. If you didn't create it already, please close this tour and start the first tour."),
               'idStep': 'link',
               'selector': '#portaltab-myfolder a',
               'text': ''},
             )}

create_it = {
    'url': '/myfolder',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Add a Page"),
    'text': "",
    'steps': ({'description': _(u"Click the [Add new...] drop-down menu."),
               'idStep': 'menu_add-new',
               'selector': '',
               'text': ''},
              {'description': _(u"Select [Page] from the menu."),
               'idStep': 'new_document',
               'selector': '',
               'text': ''},
             )}

fill_out_the_page_fields = {
    'url': '/myfolder/portal_factory/Document',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Fill out the fields"),
    'text': _(u"Now that you selected the Page content type, you need to supply some information about it."),
    'steps': ({'description': _(u"Provide a [Title] (My Page)."),
               'idStep': 'form_title',
               'selector': '',
               'text': 'My Page'},
              {'description': _(u"Provide a [Description] (This is my first Plone page.)."),
               'idStep': 'form_description',
               'selector': '',
               'text': ''},
              {'description': _(u"Add some page content (you can come back and edit this later)."),
               'idStep': '',
               'selector': '',
               'text': ''},
              {'description': _(u"[Save] the page."),
               'idStep': 'form_save',
               'selector': '',
               'text': ''},
             )}

publish_it = {
    'url': '/myfolder/my-page',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Publish the page"),
    'text': _(u"You have now created a Page for your Plone website. Before this page can be viewed by anonymous site visitors, you must publish it. Publishing also makes your page available in the Navigation portlet."),
    'steps': ({'description': _(u"Click the [State] drop-down menu."),
               'idStep': 'menu_state',
               'selector': '',
               'text': ''},
              {'description': _(u"Select [Publish] from the menu."),
               'idStep': 'content_publish',
               'selector': '',
               'text': ''},
             )}

all_done = {
    'url': '/myfolder/my-page',
    'xpath': '#plone-contentmenu-workflow dt a span.state-published',
    'xcontent': PMF(u"Published"),
    'title': _(u"All done!"),
    'text': _(u"You now have a published page in your folder."),
    'steps': ()}

ajTour = {'tourId': 'basic02_add_and_publish_a_page',
          'title': _(u"Add and publish a Page"),
          'steps': (go_to_folder,
                    create_it,
                    fill_out_the_page_fields,
                    publish_it,
                    all_done,
                   )}

