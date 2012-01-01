import cgi
from google.appengine.api import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from jinja2 import Template


class ManPage(webapp.RequestHandler):
    def get(self):
        manpageName= self.request.get('man_name')
        

