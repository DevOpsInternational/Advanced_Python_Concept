#use of search with ^ and $ sign
import re
s=re.search("^My","My name is Tejaswita Sitaram Wakhure")
if s==None:
    print("Given pattern is not at the starting of string")
else:
    print("Given pattern is at the starting of the string")
s=re.search("Wakhure$","My name is Tejaswita Sitaram waKhure",re.IGNORECASE)
if s==None:
    print("Given pattern is not at the end of string")
else:
    print("Given pattern is at the end of the string")
