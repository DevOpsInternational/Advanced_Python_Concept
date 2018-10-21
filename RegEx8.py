#use of regular expression
import re
##rgobj=re.compile("Teju")#created reg ex object
#combined compile and finditer finding either one T including zero 
miter=re.finditer("T?","Hi TTejuHello1 2 3 how are you1239 TejuWakhure,Hello TejuHi")#got iterator
count=0
for m in miter:
    count+=1
    print("Pattern found at: ",m.group(),m.end())#start gives index of found
print("Total number of times it is found is: ",count)

