'''
Created on 12/05/2012

@author: joan
'''

import webapp2
import os

from google.appengine.ext.webapp import template

class BaseHandler(webapp2.RequestHandler):
        def render(self,T,**kw):
                template_path = os.path.join(os.path.dirname(__file__), T)
                self.response.out.write(template.render(template_path,kw))
        
        def write(self, *a, **kw):
            self.response.out.write(*a,**kw)  