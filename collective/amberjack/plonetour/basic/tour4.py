from tour2 import go_to_folder
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('collective.amberjack.plonetour')
PMF = MessageFactory('plone')


welcome = go_to_folder.copy()
welcome['title'] = _(u"Add and Publish an Event")
welcome['text'] = _(u"In this tutorial, you'll create a new Event and publish it on your Plone-powered website.")


create_it = {
    'url': '/myfolder',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Create a Event"),
    'text': _("Events are useful for posting announcements about upcoming events that your company is hosting. Events function much like a page, with additional fields for adding information about an event."),
    'steps': ({'description': _(u"Click the [Add New...] drop-down menu."),
               'idStep': 'menu_add-new',
               'selector': '',
               'text': ''},
              {'description': _(u"Select [Event] from the menu."),
               'idStep': 'new_event',
               'selector': '',
               'text': ''},
             )}

fill_out_the_fields = {
    'url': '/myfolder/portal_factory/Event',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Fill out the fields"),
    'text': _(u"Now that you selected the Event content type, you need to supply some information about it."),
    'steps': ({'description': _(u"Provide a [Title] (My Event)"),
               'idStep': 'form_title',
               'selector': '',
               'text': 'My Event'},
              {'description': _(u"Provide a [Description] for your Event. <br>The description will appear in site searches and in summary listings of events on your site."),
               'idStep': 'form_description',
               'selector': '',
               'text': ''},
              {'description': _(u"Provide an [Event Location]. The location is the physical location of the event. You can describe the address or provide directions in the Body Text field."),
               'idStep': 'form_location',
               'selector': '',
               'text': ''},
              {'description': _(u"Provide the event Start and End dates."),
               'idStep': '',
               'selector': '',
               'text': ''},
              {'description': _(u"Put some content in the [Body] Text field.This is the best place to add directions to your event, information about what to expect, images, etc."),
               'idStep': '',
               'selector': '',
               'text': ''},
              {'description': _(u"Provide an Event Type by typing in the New Categories field. Typical event types include: Fundraiser, Auction, Sale, Concert, Performance, etc. Once you have added a new event type, it will appear for selection in the Existing Categories field the next time you create an event."),
               'idStep': '',
               'selector': '',
               'text': ''},
               {'description': _(u"Provide contact information in the remaining fields."),
               'idStep': '',
               'selector': '',
               'text': ''},
              {'description': _(u"Click Save to finish."),
               'idStep': 'form_save',
               'selector': '',
               'text': ''},
             )}

publish_it = {
    'url': '/myfolder/my-event',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Publish the event"),
    'text': _(u"In order for anonymous site visitors to see your event you must publish it first. Publishing also makes your event available in the event portlet and event collection."),
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
    'url': '/myfolder/my-event',
    'xpath': '#plone-contentmenu-workflow dt a span.state-published',
    'xcontent': PMF(u"Published"),
    'title': _(u"All done!"),
    'text': _(u"You now have a published event in your folder."),
    'steps': ()}

ajTour = {'tourId': 'basic04_add_and_publish_an_event',
          'title': _(u"Add and publish an Event"),
          'steps': (welcome,
                    create_it,
                    fill_out_the_fields,
                    publish_it,
                    all_done,
                   )}

