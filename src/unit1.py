'''
Created on 12/05/2012

@author: joan
'''

form = '''
        <form method="post" action="/testform">
            <input name="q">
            <input type="submit">
        </form>'''

import webapp2



class MainHandler(webapp2.RequestHandler):
    def get(self):
            
        
        self.response.out.write(form)

class TestHandler(webapp2.RequestHandler):
    def get(self):
            
        q = self.request.get('q')
        self.response.out.write(q)

