#use of destructor
import sys
import time
class Test:
    def __init__(self,name):
        self.name=name
        print("I am doing initialisation")
    def __del__(self):
        print("I am doing cleanup activity")
L1=[Test("Teju"),Test("Ashi"),Test("Mani")]


print(L1[0].name)
print(sys.getrefcount(L1[0]))
print("End of application")
