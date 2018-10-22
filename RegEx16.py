#use of function replacement in regular expression
#subn
import re
s=input("Enter string to be replaced")
t=input("Enter target string")
u=re.subn("\d",s,t)
print("The result of the operation is: ",u[0])
print("The number of replacement happened are: ",u[1])
