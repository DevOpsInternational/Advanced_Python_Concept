#abstract method
from abc import *
class S(ABC):
    @abstractmethod
    def m1(self):        
        pass
    @abstractmethod
    def m2(self):        
        pass
    @abstractmethod
    def m3(self):        
        pass
class T(S):
    def m1(self):
        print("I am implementing parent class method m1()")
    def m2(self):
        print("I am implementing parent class method m2()")
class C(T):
    def m3(self):
        print("I am implementing parent T class method m3()")
t=C()
t.m1()
t.m2()
t.m3()
s=S()

    
    
