'''
Created on 03/06/2012

@author: joan
'''


def WikiHandler(BaseHandler):
    
    def render(self, template, **kw):
        kw['userTemplate'] = 'WikiBase.html'
        
        super.render(template, **kw)
