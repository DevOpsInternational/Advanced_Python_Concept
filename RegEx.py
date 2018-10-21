#use of regular expression
import re
rgobj=re.compile("Teju")#created reg ex object
miter=rgobj.finditer("Hi Teju how are you Teju,Hello Teju")#got iterator
count=0
for m in miter:
    count+=1
    print("Pattern found at: ",m.start())#start gives index of found
print("Total number of times it is found is: ",count)
