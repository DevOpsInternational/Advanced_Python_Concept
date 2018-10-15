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
