#abstract method
from abc import *
class Student(ABC):
    @abstractmethod
    def m1(self):        
        print("I am abtract method")
s1=Student()
s1.m1()
