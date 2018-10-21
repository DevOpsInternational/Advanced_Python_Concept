#use of search function in Regular Expression
import re
s=input("Enter string to be search")
t=input("Enter string to be match")
m=re.search(s,t)
if   m!=None:
    print("String got searched using search function: ",m.start(),m.end())
else:
    print("String not found in given string")
