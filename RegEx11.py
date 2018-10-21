#use of function match in regular expression
import re
s=input("Enter string to be matched")
m=re.match(s,"My name tejaswita wakhure")
if(m!=None):
    print("Match is available at the begining of the string")
    print("Index is {}and end at {}".format(m.start(),m.end()))
else:
    print("Match is not avilable at the begining of the string")
