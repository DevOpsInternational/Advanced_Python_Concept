#Regular expression to find valid mobile number
import re
n=input("Enter mobile number")
v=re.fullmatch("[+][9][1][6-9]\d{9}",n)
if v!=None:
    print("It is a valid mobile number in India")
else:
    print("It is not valid mobile number in India")
