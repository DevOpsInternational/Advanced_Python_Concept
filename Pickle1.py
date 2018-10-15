import pf
from pickle import*
#pickling
f=open("pf.dat","wb")
n=int(input("Enter number of Employees"))
for i in range(n):
    eno=int(input("Enter employee number"))
    ename=input("Enter employee name")
    esal=int(input("Enter employee salary"))
    eadd=input("Enter employee Address")
    e=pf.Emp(eno,ename,esal,eadd)
    dump(e,f)
f.close()
