#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os

from google.appengine.ext.webapp import template

from BaseHandler import BaseHandler

#Homeworks
from unit2 import *
from unit1 import *           

from Blog import BlogFront
from Blog import PostPage
from Blog import NewPost
from Blog import Register
from Blog import Welcome as WelcomeBlog
from Blog import Login
from Blog import Logout

from handlers.Signup import Register as WikiRegister
from handlers.Signup import Login as WikiLogin
from handlers.Signup import Logout as WikiLogout
from handlers.Signup import Register as WikiRegister

from handlers.Wiki import EditPage
from handlers.Wiki import VisitPage
from handlers.Wiki import FrontPage as WikiFrontPage
from handlers.Wiki import HistPage
PAGE_RE = r'((?:[a-zA-Z0-9_-]+/?)*)'

from handlers.Wiki import Welcome as WelcomeWiki
wiki_handlers= [('/wiki/signup/?',WikiRegister),
                #('/wiki/?',WikiFrontPage),
                ('/wiki/login/?',WikiLogin),
                ('/wiki/logout/?',WikiLogout),
                ('/wiki/register/?',WikiRegister),
                ('/wiki/welcome/?',WelcomeWiki),
                ('/wiki/_history/'+PAGE_RE+"",HistPage),
                ('/wiki/_edit/'+PAGE_RE,EditPage),
                ('/wiki/'+PAGE_RE,VisitPage),
                
                
                ]

app = webapp2.WSGIApplication([('/', MainHandler),('/testform', TestHandler),
                               ("/unit2/rot13", ROT13),("/unit2/signup",Signup),("/unit2/welcome",Welcome),
                               ("/blog/?(?:\.json)?", BlogFront),
                               ("/blog/([0-9]+)(?:\.json)?", PostPage),
                               ("/blog/newpost", NewPost),
                               ("/newpost", NewPost),
                               ("/(?:\.json)?", BlogFront),
                               ("/([0-9]+)(?:\.json)?", PostPage),
                               ("/signup",Register),
                               ("/welcome",WelcomeBlog),
                               ("/login",Login),
                               ("/logout",Logout)
                               ]+wiki_handlers,
                              debug=True)

