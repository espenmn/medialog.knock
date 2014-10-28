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
            context = self.context
            mailhost = self.context.MailHost
            form= self.request.form
            hjemmestyrkene=form.get('hjemme')
            sumHjemme=form.get('sumHjemme')
            mto = 'espen@medialog.no'
            msg="""
            Hjemmestyrkene: %s tilsammen kr %s    """ %(hjemmestyrkene, sumHjemme)

            mailhost.send(messageText=msg, subject='Bestilling', mto=mto, mfrom='post@medialog.no')
            return "takk for din bestilling"

     	return self.index()
 
