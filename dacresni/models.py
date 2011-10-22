# models 
from gooogle.appengine.ext import db
from gooogle.appengine.api import users

class Manual(db.Model):
    name = db.StringProperty(required=True)
    date = db.DateProperty()
    content = db.TextProperty()
    section = db.IntegerProperty()
    
class Function(db.Model):
    name = db.StringProperty(required=True)
    #params = db.StringProperty()
    #I've been considering the utility of a parameter list for a while
    headers = db.StringList(required=Ture)
    manual = db.Reference(Manual)






