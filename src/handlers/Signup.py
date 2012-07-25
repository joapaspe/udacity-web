'''
Created on 01/06/2012

@author: joan
'''

import re

from BaseHandler import BaseHandler
from models.User import User


USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$") 
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE = re.compile(r'^[\S]+@[\S]+\.[\S]+$')

def valid_email(email):
    return not email or EMAIL_RE.match(email)

class Signup(BaseHandler):
    def get(self):
        
        self.render("signup.html")
    
    def post(self):
                
        have_error = False
        self.username = self.request.get('username')
        self.password = self.request.get('password')
        self.verify = self.request.get('verify')
        self.email = self.request.get('email')
        
        params = {'username':self.username, 'email':self.email}
    
        if not valid_username(self.username):
         params['error_username'] = "That's not a valid username."
         have_error = True
    
        if not valid_password(self.password):
            params['error_password'] = "That wasn't a valid password."
            have_error = True
        elif self.password!=self.verify:
            params['error_verify'] = "Your passwords didn't match."
            have_error = True
            
        if not valid_email(self.email):
            params['error_email'] = "That's not a valid email."
            have_error = True
        
        if have_error:
            self.render("signup.html",**params)
        else:
            self.done()
            
        def done():
            raise NotImplementedError()
        
class Login(BaseHandler):
    def get(self):
        self.render("login.html")
    
    def post(self):
        
        
        have_error = False
        
        self.username = self.request.get('username')
        self.password = self.request.get('password')
        u = User.login(self.username, self.password)
        
        
        if not u:
            msg = 'Invalid login.'
            self.render('login.html', error_message = msg)
            return
        
        self.login(u)
        self.redirect("/wiki/")
        #self.render("welcome.html", username = self.username)
        
class Logout(BaseHandler):
    def get(self):
        self.logout()
        self.redirect('/wiki/')
        
class Register(Signup):
    def done(self):
        #make sure the user doesn't already exist
        u = User.by_name(self.username)
        if u:
            msg = 'That user already exists.'
            self.render('signup.html', error_username = msg)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()

            self.login(u)
            self.redirect("/wiki/")
            self.render("welcome.html", username = self.username)
 
 