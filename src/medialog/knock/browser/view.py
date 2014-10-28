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

    def __call__(self,REQUEST):
    	if 'send.order' in self.request.form: 
    		#return "hello world"
    		context = self.context
    		return self.request.form['hjemme']

        return self.index()
 
