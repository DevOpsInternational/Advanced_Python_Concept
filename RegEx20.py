#to check valid identifier or not
import re
s=input("Enter the identifier to be matched")
m=re.fullmatch("[a-k][0369][a-zA-Z0-9#]*",s)
if m!=None:
    print("It is valid language identifier")
else:
    print("It is not valid language identifier")
