#use of function replacement in regular expression
#sub
import re
s=input("Enter string to be replaced")
t=input("Enter target string")
u=re.sub("\d",s,t)
print(u)
