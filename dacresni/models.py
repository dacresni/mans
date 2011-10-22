# models 
from gooogle.appengine.ext import db
from gooogle.appengine.api import users

class Manual(db.Model):
    name = db.StringProperty(required=True)
    date = db.DateProperty()
    content = db.TextProperty()
    section = db.IntegerProperty()
    




