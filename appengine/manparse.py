# a file to parse the code of the man pages 
import re
from google.appengine.ext import db
from Models import Manual, Function
# the following strings are to regular expressions to find 
name_pattern=re.compile(r"^.Nm",re.DEBUG)
date_string=re.compile(r"^.Dd",re.DEBUG)
headder_pattern=re.compile( r"^.Fd"re.DEBUG)
function_name_pattern=re.compile(r"^.BR"re.DEBUG)
patterns = { "name":name_pattern,
        "date": date_string, 
        "headder":headder_pattern,
        "function":function_name_pattern }

docstring=   """ takes a block of text and a dictionary{"name":pattern}  of compiled regex patterns returns a {name:results} dictionary
def scan(block):
    """
def scan(file):
        result = {"name":"",
                "date","",
                "headder":[],
                "function":[]
                "whatis":""}
        for line in file:
            if line.beginswith(".Dd")
               result["date"]=line
            if line.beginswith(".Nm")
               result["name"]=line
            if line.beginswith(".Nd")
               result["whatis"]=line
            if line.beginswith(".Fo")
               result["function"].append(line)
            if line.beginswith(".In")
               result["headder"].append(line)


def names():
    for page in os.listdir("."):
        manname = page.split(".")[0]
        man = open(manname, 'r')
        scan(man))
        #newman = Manual(manname,)
#action 


if __name__ == '__main__' :
    names()
