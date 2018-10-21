#use of find all matches and return in the string
import re
s=input("Enter string")
t=input("Enter string to be matched")
m=re.findall(t,s)
if m!=0:
    print("Found: ",m)
else:
    print("Not found")
