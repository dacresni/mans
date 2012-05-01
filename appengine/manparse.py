# a file to parse the code of the man pages 
import re

# the following strings are to regular expressions to find 
date_string="^.Dd"
name_pattern="^.Nm"
headder_pattern="^.Fd"
function_name_pattern="^.BR"

