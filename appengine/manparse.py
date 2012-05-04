# a file to parse the code of the man pages 
import re
from google.appengine.ext import db
from Models import Manual, Function
# the following strings are to regular expressions to find 
name_pattern=re.compile("^.Nm",re.DEBUG)
date_string=re.compile("^.Dd",re.DEBUG)
headder_pattern=re.compile( "^.Fd"re.DEBUG)
function_name_pattern=re.compile("^.BR"re.DEBUG)
def scan(block, patterns):
    """ takes a block of text and a dictionary{"name":pattern}  of compiled regex patterns returns a {name:results} dictionary
    """
    for pat in patterns.viewkeys:
        pat.search(b)


def names():
    for page in os.listdir("."):
        manname = page.split(".")[0]
        scan(manname, )       
        newman = Manual(manname,)
#action 


if __name__ == '__main__' :
    names()
