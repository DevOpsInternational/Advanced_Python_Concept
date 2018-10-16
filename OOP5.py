#use of static variable
class Student:
    c="AVCOE"
    def __init__(self,n=" ",m=0):
        self.t=n
        self.t1=m
    def disp(self):
        t=100
        self.t=200
        print("Value of local t is: ",t)
        print(" t is: ",self.t)
        print(" t1 is: ",self.t1)
        print("College name as: ",Student.c)
s=Student()
Student.c="COEPPune"
print(s.c)
s.disp()
s2=Student()
s2.disp()
