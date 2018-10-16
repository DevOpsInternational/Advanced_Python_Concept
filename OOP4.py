#constructor with multiple arguments
class Student:
    def __init__(self,n=" ",m=0):
        self.t=n
        self.t1=m
    def disp(self):
        t=100
        self.t=200
        print("Value of local t is: ",t)
        print(" t is: ",self.t)
        print(" t1 is: ",self.t1)
s=Student()
##self.t1=8
s.t=900
print(s.t)
s.disp()
