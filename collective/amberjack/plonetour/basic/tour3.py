from zope.i18nmessageid import MessageFactory
_ = MessageFactory('collective.amberjack.plonetour')
PMF = MessageFactory('plone')

go_to_folder = {
    'url': '/',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Add and Publish a News Item"),
    'text': _(u"In this tutorial, you'll create a new News Item and publish it on your Plone-powered website."),
    'steps': ({'description': _(u"Navigate to the folder called [MyFolder] that you created in a previous tutorial."),
               'idStep': 'link',
               'selector': '#portaltab-myfolder a',
               'text': ''},
             )}

add_and_publish_a_page = {
    'url': '/myfolder',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Add and Publish a News Item"),
    'text': "",
    'steps': ({'description': _(u"First, click the [Add New...] drop-down menu"),
               'idStep': 'menu_add-new',
               'selector': '',
               'text': ''},
              {'description': _(u"Select [News Item] from the menu"),
               'idStep': 'new_news',
               'selector': '',
               'text': ''},
             )}

now_fill_out_the_page_fields = {
    'url': '/myfolder/portal_factory/News Item',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Now that you've select the News Item content type, you'll need to supply some information about the it"),
    'text': _(u""),
    'steps': ({'description': _(u"Provide a [Title] (My News)"),
               'idStep': 'form_title',
               'selector': '',
               'text': 'My News'},
              {'description': _(u"Provide a [Description] (This is my first Plone News Item)"),
               'idStep': 'form_description',
               'selector': '',
               'text': 'This is my first Plone News Item'},
              {'description': _(u"Add some page content (you can come back and edit this later)"),
               'idStep': '',
               'selector': '',
               'text': ''},
              {'description': _(u"[Save] the page"),
               'idStep': 'form_save',
               'selector': '',
               'text': ''},
             )}

publish_the_page = {
    'url': '/myfolder/my-news',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Publish the news"),
    'text': _(u"You have now created a News Item for your Plone website. Before this news can be viewed by anonymous site visitors, you must publish it. Publishing also makes your news available in the Navigation portlet."),
    'steps': ({'description': _(u"Click the [State] drop-down menu"),
               'idStep': 'menu_state',
               'selector': '',
               'text': ''},
              {'description': _(u"Select [Publish] from the menu"),
               'idStep': 'content_publish',
               'selector': '',
               'text': ''},
             )}

all_done = {
    'url': '/myfolder/my-news',
    'xpath': '#plone-contentmenu-workflow dt a span.state-published',
    'xcontent': PMF(u"Published"),
    'title': _(u"All done!"),
    'text': _(u"All done!"),
    'steps': ()}

ajTour = {'tourId': 'add_and_publish_a_news',
          'title': _(u"Add and publish a news item"),
          'steps': (go_to_folder,
                    add_and_publish_a_page,
                    now_fill_out_the_page_fields,
                    publish_the_page,
                    all_done,
                   )}

