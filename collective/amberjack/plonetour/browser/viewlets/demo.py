# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets import common

class DemoViewlet(common.ViewletBase):
    """Viewlet for the demo"""
    
    render = ViewPageTemplateFile('demo.pt')
    
    def __init__(self, context, request, view, manager): 
        self.context = context 
        self.request = request  
        
    def site(self):
        return self.context.portal_url()