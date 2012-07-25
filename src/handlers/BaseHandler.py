'''
Created on 01/06/2012

@author: joan
'''

import webapp2
import jinja2
import os

from utils.HashUtils import *
from models.User import User
template_dir = os.path.join(os.path.dirname(__file__), '../templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = False)




class BaseHandler(webapp2.RequestHandler):
    
        
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)


    def render(self, template, **kw):
       self.write(self.render_str(template, **kw))
    
    def render_json(self,d):
        json_txt = json.dumps(d)
        self.response.headers['Content-Type'] = 'application/json; charset=UTF-8'
        self.write(json_txt)

    def set_secure_cookie(self,name,val):
        cookie_val = make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/'% (name,cookie_val))
        
    def read_secure_cookie(self,name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and check_secure_val(cookie_val)
    
    def login(self,user):
        self.set_secure_cookie('user_id', str(user.key().id()))
        
    def logout(self):
        self.response.headers.add_header('Set-Cookie','user_id=; Path=/')
        
    def initialize(self, *a, **kw):
        
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        
        self.user = uid and User.by_id(int(uid))
        
        #Enviroment globals variables
        jinja_env.globals['HOST_URL'] = self.request.host_url
        jinja_env.globals['USER'] = self.user
        if self.request.url.endswith('.json'):
            self.format = 'json'
        else:
            self.format = 'html'