#pickling and unpickling
from pickle import *
class Emp:
    def __init__(self,eno,ename,esal,eadd):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eadd=eadd
    def disp(self):
        print("Employee Number is: ",self.eno)
        print("Employee Name is: ",self.ename)
        print("Empolyee Salary is: ",self.esal)
        print("Employee Address is: ",self.eadd)
e=Emp(184,"Tejaswita",70000,"Bengluru")
with open("PickleFile1.txt","wb") as f:
    dump(e,f)
    print("Pickling of Employee is completed")
with open("PickleFile1.txt","rb") as f:
    obj=load(f)
    print("Unpickling of Employee is completed",obj.disp())
