from zope.i18nmessageid import MessageFactory
_ = MessageFactory('collective.amberjack.plonetour')
PMF = MessageFactory('plone')

"""
XXX things to be done:
 - enter text in kupu
 - press the save button: submitting the form has a "strange" behaviour, it reload the portlet configuration. .click() tries to exit the page so ask a confirmation
"""

welcome_message = {
    'url': '/',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Create a static text portlet"),
    'text': _(u"In this tutorial, you'll create a static text portlet on your Plone-powered website.<br/>Portlets are the boxes in the left and right side columns of your site. You probably already have a News, Events and Navigation portlets although depending on the type of content on your site, you may not see them currently. There are many portlets types available for you to use, however this tutorial will cover the Static Text portlets. <br />Navigate to the homepage of your site. It is important that you access portlet management from the homepage."),
    'steps': ({'description': _(u"Click the [Manage Portlets] link in the lower left or right corner of the page."),
               'idStep': 'manage_portlets',
               'selector': '',
               'text': ''},
               )}


add_portlet = {
    'url': '/@@manage-portlets',
    'xpath': '',
    'xcontent': '',
    'title': _(u"Add a portlet"),
    'text': _(u"You are now looking at the Manage Portlets page. Notice that there are a set of menus and buttons on both the left and right side of the screen. Each set controls its corresponding column. Also note that if you have portlets already added to the site, you will see their names listed here."),
    'steps': ({'description': _(u"Click the Add [Portlet drop-down] menu for either the left or right column.<br />Then select [Static Text Portlet] from the menu."),
               'idStep': 'select',
               'selector': 'div[@id="portletmanager-plone-leftcolumn"] select[@name=":action"]',
               'text': '/++contextportlets++plone.leftcolumn/+/plone.portlet.static.Static'},
             )}

configure_portlet = {
    'url': '/', # also other http://localhost:8080/site/++contextportlets++plone.leftcolumn/+/plone.portlet.static.Static
    'xpath': 'h1.documentFirstHeading',
    'xcontent': PMF(u'Add static text portlet'),
    'title': _(u"Configure the portlet"),
    'text': _(u"You are now looking at the Static Text Portlet edit screen. This type of portlet allows you to use the same visual editor you have been using for other content types. A static text portlet can be used to insert a clickable image such as a donation button, a series of external links, or other content you wish to post."),
    'steps': ({'description': _(u"In the [Portlet Header] field type 'Sample Portlet'."),
               'idStep': 'form_header',
               'selector': '',
               'text': 'Sample Portlet'},
               {'description': _(u"Now type some text or insert an image if you wish into the [Body Text] field. Since a portlet is much smaller than a page, be sure to keep the content fairly short."),
               'idStep': 'form_content', #XXX
               'selector': '',
               'text': _(u'something')},
               {'description': _(u"The [Omit Portlet Border] checkbox can be checked if you wish to not display the Portlet Header or Footer. Leave this box unchecked for now."),
               'idStep': 'checkbox',
               'selector': 'input[name=form\\.omit_border]',
               'text': 'checked'},
               {'description': _(u"Type some text into the Portlet Footer field if you wish. You can make the [Portlet Footer] text clickable by typing or pasting a web address into the [Details Link] field."),
               'idStep': 'form_footer',
               'selector': '',
               'text': _(u'text in the footer')},
               {'description': _(u"Notice the [Hide Portlet] checkbox. You can use this checkbox to temporarily hide your portlet without losing the content. Leave this box unchecked for now."),
               'idStep': '',
               'selector': '',
               'text': ''},
               {'description': _(u"Click [Save] to finish."), # XXX
               'idStep': '',
               'selector': '',
               'text': ''},
             )}

view_portlet = {
    'url': '/@@manage-portlets',
    'xpath': 'div[@class="portletHeader"] a:contains("Sample Portlet")',
    'xcontent': 'aj_xpath_exists',
    'title': _(u"View the portlet"),
    'text': _(u"Now that you have created your first portlet, let's take a look at it."),
    'steps': ({'description': _(u"Navigate back to the [homepage] of your site. Since you do not have your normal navigation tabs in the Manage Portlets page, try clicking on the site logo.'."),
               'idStep': 'go_home',
               'selector': '',
               'text': ''},
             )}

all_done = {
    'url': '/',
    'xpath': '.portlet-static-sample-portlet',
    'xcontent': 'aj_xpath_exists',
    'title': _(u"All done!"),
    'text': _(u"You should see the new portlet you added in the column you chose to add it to. This portlet will now appear on all pages on the site, including new ones that you might create. If you wish to rearrange the order of your portlets, or remove a portlet, return to the Manage Portlets page and use the directional arrows to move portlets or the red X delete a portlet."),
    'steps': ()}

ajTour = {'tourId': 'basic12_create_a_static_text_portlet',
          'title': _(u"Create a static text portlet"),
          'steps': (welcome_message,
                    add_portlet,
                    configure_portlet,
                    view_portlet,
                    all_done,
                   )}

