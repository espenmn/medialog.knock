#coding: utf-8


from Products.Five import BrowserView

from plone.dexterity.utils import iterSchemata, resolveDottedName
from zope.schema import getFields
from plone.dexterity.interfaces import IDexterityContent

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

try:
    from zope.app.component.hooks import getSite
except ImportError:
    from zope.component.hooks import getSite

class Videresalg(BrowserView):
    
    index = ViewPageTemplateFile("videresalg.pt")
    
    
    def render(self):
        return self.index()

    def __init__(self, context, request):
        super(Exporter, self).__init__(context, request)
    
    def __call__(self,REQUEST):
        return self.index()

   
    def export_images(self, imagesize):
        '''Returns the file (with the preview images
        '''
        return "hello world"
       


