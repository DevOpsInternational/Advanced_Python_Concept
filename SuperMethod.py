#use of super method
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def h(self):
        print("For software engineer python learning is very easy")
class SE(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def disp(self):
        print("Python is very easy for SW People")
s=SE("Tejaswita",28,189,100000)
s.disp()
s.h()
