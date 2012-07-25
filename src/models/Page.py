'''
Created on 01/06/2012

@author: joan
'''

from google.appengine.ext import db
from utils.HashUtils import *
from models.User import User 

def add_page(page):
    page.put()

def page_key(name='default'):
    return db.Key.from_path('pages',name)

class Page(db.Model):
    name= db.StringProperty()
    content = db.TextProperty(required = True)
    creation_data = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now_add = True)
    user = db.ReferenceProperty(User,required = True)
    original = db.SelfReference(collection_name='history_pages')
    
    @classmethod
    def by_name(cls, name):
        p = Page.all().filter('name =', name).get()
        return p
    
    def get_hist(self):
            return self.history_pages
        
        
 