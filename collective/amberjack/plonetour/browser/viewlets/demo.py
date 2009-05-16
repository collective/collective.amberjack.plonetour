# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common

class DemoViewlet(common.ViewletBase):
    """Viewlet for the demo"""
    
    render = ViewPageTemplateFile('demo.pt')