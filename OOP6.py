#Passing member of one class to another class
class Employee:
    def __init__(self,ename,eno,esal,ead):
        self.ename=ename
        self.eno=eno
        self.esal=esal
        self.ead=ead
    def disp(self):
        print("Name of the employee is: ",self.ename)
        print("Number of employee is: ",self.eno)
        print("Salary of Employee is: ",self.esal)
        print("Employee address is: ",self.ead)
class Updation:
    def Emp(emp):#it is refernce to created employee object
##        print("Employee number is: ",emp.eno)
        emp.esal=emp.esal+10000
##        print("Updated salary of",emp.eno,"is: ",emp.esal)
        emp.disp()


e1=Employee("Tejaswita",168,70000,"Bengluru")
e1.disp()
e2=Employee("Meera",123,50000,"Mumbai")
e2.disp()
Updation.Emp(e1)
Updation.Emp(e2)
##e1.disp()
##e2.disp()
