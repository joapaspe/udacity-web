from BaseHandler import BaseHandler
from models.Page import * 

from datetime import datetime
class Welcome(BaseHandler):
    def get(self):
        
        if self.user:
                
            self.render("welcome.html", username = self.user.name)
        else:
            self.redirect("/wiki/signup")


class FrontPage(BaseHandler):
    
    def get(self):
        
        #TODO: Check if created
        self.render("baseWiki.html")
        
class VisitPage(BaseHandler):
    
    def get(self,namepage):
        
        #TODO: Check if created
        
        p =  Page.by_name(namepage)
        if p:
            self.render("visitPage.html",content = p.content,namepage=namepage)
        else:
            if not self.user:
                self.redirect("/wiki/register")
                return
            
            self.redirect("/wiki/_edit/%s" % namepage)
    

class EditPage(BaseHandler):
    
    def get(self,namepage):
        
        #TODO: Check if created
        content = ""
        
        if not self.user:
                self.redirect("/wiki/"+namepage)
                return
            
        p =  Page.by_name(namepage)
        
        if p:
            content = p.content
        self.render("editPage.html",namepage=namepage,content=content,edit=True)
        
        
    def post(self,namepage):
        #TODO save the page
        
        content = self.request.get('content')
    
        if content:
            p =  Page.by_name(namepage)
            if p:
                phist = Page(parent = page_key(), name = namepage, content = p.content, creation_data = p.last_modified,history=p,user=p.user,original=p) 
                p.content = content
                p.last_modified = datetime.now()
                p.put()
                phist.put()
            else:
                p = Page(parent = page_key(), name = namepage, content = content,user= self.user)
                p.put()
                p.original = p
                p.put()
            
            self.redirect('/wiki/%s'%namepage)
        else:
            error = "No content!"
            self.render("editPage.html",error=error,content = content)   
        
class HistPage(BaseHandler):
    
    def get(self,namepage):
        
        #TODO: Check if created
        content = ""
                            
        p =  Page.by_name(namepage)
        
        if p:
            hist = p.get_hist()
            self.render("histPage.html",namepage=namepage,hist=hist,edit=True)
        
        