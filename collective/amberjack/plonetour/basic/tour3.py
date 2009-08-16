from tour2 import go_to_folder
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('collective.amberjack.plonetour')
PMF = MessageFactory('plone')


welcome = go_to_folder.copy()
welcome['title'] = _(u"Add and publish a News Item")
welcome['text'] = _(u"In this tutorial, you'll create a new News Item and publish it on your Plone-powered website.")


create_it = {
    'url': '/myfolder',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Create a News Item"),
    'text': "",
    'steps': ({'description': _(u"Click the [Add new...] drop-down menu."),
               'idStep': 'menu_add-new',
               'selector': '',
               'text': ''},
              {'description': _(u"Select [News Item] from the menu."),
               'idStep': 'new_news',
               'selector': '',
               'text': ''},
             )}

fill_out_the_fields = {
    'url': '/myfolder/portal_factory/News Item',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Fill out the fields"),
    'text': _(u"Now that you selected the News Item content type, you need to supply some information about it."),
    'steps': ({'description': _(u"Provide a [Title] (My News)."),
               'idStep': 'form_title',
               'selector': '',
               'text': 'My News'},
              {'description': _(u"Provide a [Description] for your News Item. <br />The description will appear in site searches and in summary listings of news on your site."),
               'idStep': 'form_description',
               'selector': '',
               'text': ''},
              {'description': _(u"Put some content in the Body Text field."),
               'idStep': '',
               'selector': '',
               'text': ''},
              {'description': _(u"Notice the Upload Image field at the bottom of the page. You can attach an image to a News Item which will appear in summary listings of News Items. You can also caption the image."),
               'idStep': '',
               'selector': '',
               'text': ''},
              {'description': _(u"Click [Save] to finish."),
               'idStep': 'form_save',
               'selector': '',
               'text': ''},
             )}

publish_it = {
    'url': '/myfolder/my-news',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Publish the news item"),
    'text': _(u"In order for anonymous site visitors to see your news item you must publish it first. Publishing also makes your news item available in the news portlet and news collection."),
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
    'url': '/myfolder/my-news',
    'xpath': '#plone-contentmenu-workflow dt a span.state-published',
    'xcontent': PMF(u"Published"),
    'title': _(u"All done!"),
    'text': _(u"You now have a published news item in your folder."),
    'steps': ()}

ajTour = {'tourId': 'basic03_add_and_publish_a_news_item',
          'title': _(u"Add and publish a News Item"),
          'steps': (welcome,
                    create_it,
                    fill_out_the_fields,
                    publish_it,
                    all_done,
                   )}

