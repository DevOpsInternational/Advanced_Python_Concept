#use of function fullmatch in regular expression
import re
s=input("Enter string to be matched")
m=re.fullmatch(s,"abc$")
if(m!=None):
    print("Complete match found for the string:",m.start(),m.end())
else:
    print("No complete match found for the string")
