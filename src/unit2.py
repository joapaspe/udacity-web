'''
Created on 12/05/2012

@author: joan
'''
import re

from BaseHandler import BaseHandler


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
            self.redirect('/unit2/welcome?username='+self.username)

class Welcome(BaseHandler):
    def get(self):
        username = self.request.get('username')
       
              
        if valid_username(username):
            
            self.render("welcome.html", username = username)
        else:
            self.redirect("/unit2/signup")

class ROT13(BaseHandler):
        def get(self):
            self.render("rot13-form.html")
            
        def post(self):
                rot13 = ""
                text = self.request.get('text')
                if text:
                     rot13 = text.encode("rot13")
                     
                self.render("rot13-form.html",text=rot13)