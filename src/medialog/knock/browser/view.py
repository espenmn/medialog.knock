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
            sumHjemmestyrkene=form.get('sumHjemmestyrkene')
            sumToralv= form.get('sumToralv')
            sumFarmorfortalte = form.get('sumFarmorfortalte')
            sumFarmorseventyr = form.get('sumFarmorseventyr') 
            sumSemedkamera = form.get('sumSemedkamera') 
            sumHjemmefronten = form.get('sumHjemmefronten')               
            sumRjukan = form.get('sumRjukan')          
            sumKaaresbok = form.get('sumKaaresbok') 
            sumViul = form.get('sumViul')
            sumBeisfjord = form.get('sumBeisfjord')
            sumAlt = form.get('sumAlt')
            
            hjemmestyrkene=form.get('hjemmestyrkene')
            toralv= form.get('toralv')
            farmorfortalte = form.get('farmorfortalte')
            farmorseventyr = form.get('farmorseventyr') 
            semedkamera = form.get('semedkamera') 
            hjemmefronten = form.get('hjemmefronten')               
            rjukan = form.get('rjukan')          
            kaaresbok = form.get('kaaresbok') 
            viul = form.get('viul')
            beisfjord = form.get('beisfjord')
            navn = form.get('navn')
            epost = form.get('epost')
            telefon = form.get('telefon')
            firma  = form.get('firma')
            adresse = form.get('adresse')
            postnr = form.get('postnr')
            poststed = form.get('poststed') 
 
            
            mto = 'arnekjeldstadli@gmail.com, espen@medialog.no'
            msg="""
            Hjemmestyrkene: %s tilsammen kr %s    
            Toralv: %s tilsammen kr %s  
            Farmorfortalte: %s tilsammen kr %s  
            Farmorseventyr: %s tilsammen kr %s  
            Semedkamera: %s tilsammen kr %s  
            Hjemmefronten:   %s tilsammen kr %s  
            Rjukan: %s tilsammen kr %s  
            Kaaresbok: %s tilsammen kr %s  
            Viul: %s tilsammen kr %s  
            Beisfjord: %s tilsammen kr %s  
            Totalt: %s
            Navn: %s Epost: %s Telefon: %s Firma: %s Adresse: %s Postnr: %s Poststed: %s
            """  %(hjemmestyrkene, sumHjemmestyrkene,
            	 toralv, sumToralv,
            	 farmorfortalte, sumFarmorfortalte,
            	 farmorseventyr, sumFarmorseventyr,
            	 semedkamera, sumSemedkamera,
            	 hjemmefronten, sumHjemmefronten,
            	 rjukan, sumRjukan,
            	 kaaresbok, sumKaaresbok,
            	 viul, sumViul,
            	 beisfjord, sumBeisfjord,
            	 sumAlt,
            	 navn, epost, telefon, firma, adresse, postnr, poststed, 
            	)
            

            mailhost.send(messageText=msg, subject='Bestilling', mto=mto, mfrom='post@medialog.no')
            return "takk for din bestilling"

     	return self.index()
 
 
class Harrys(BrowserView):
    
    index = ViewPageTemplateFile("harrys.pt")
    
    
    def render(self):
        return self.index()

    def __call__(self,REQUEST):
        if 'send.order' in self.request.form: 
            context = self.context
            mailhost = self.context.MailHost
            form= self.request.form
            sumHarrysrode=form.get('sumHarrysrode')
            sumHarryshvite=form.get('sumHarryshvite')
            sumHarrysol=form.get('sumHarrysol')            
            
            sumAlt = form.get('sumAlt')
            
            harryshvite=form.get('harryshvite')
            harrysrode=form.get('harrysrode')
            harrysol=form.get('harrysol')
            
            
            navn = form.get('navn')
            epost = form.get('epost')
            telefon = form.get('telefon')
            firma  = form.get('firma')
            adresse = form.get('adresse')
            postnr = form.get('postnr')
            poststed = form.get('poststed') 
 
            
            mto = 'arnekjeldstadli@gmail.com, espen@medialog.no'
            msg="""
            Harrys Rode: %s tilsammen kr %s    
            Harrys Hvite: %s tilsammen kr %s  
            Harrys Ol: %s tilsammen kr %s  
            
            Totalt: %s
            Navn: %s Epost: %s Telefon: %s Firma: %s Adresse: %s Postnr: %s Poststed: %s
            """  %(harrysrode, sumHarrysrode,
            	 harryshvite, sumHarryshvite,
            	 harrysol, sumHarrysol,
            	 sumAlt,
            	 navn, epost, telefon, firma, adresse, postnr, poststed, 
            	)
            

            mailhost.send(messageText=msg, subject='Bestilling', mto=mto, mfrom='post@medialog.no')
            return "takk for din bestilling"

     	return self.index()
 

