#use of has-A relationshhip
class Car:
    def __init__(self,model,price,name):
        self.model=model
        self.price=price
        self.name=name
    def getinfo(self):
        print("Car model is: ",self.model)
        print("Car Model name is: ",self.name)
        print("Car price is: ",self.price)
class Emp:
    def __init__(self,eno,ename,esal,car):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.car=car
    def disp(self):
        print("Employee number is: ",self.eno)
        print("Employee name is: ",self.ename)
        print("Employee salary is: ",self.esal)
        print("Employee car is:")
        self.car.getinfo()
c=Car("SUVz",2500000,"Fortuner")
e=Emp(189,"Tejaswita",100000,c)
e.disp()
