#use of destructor
import time
class Test:
    def __init__(self):
        print("I am doing initialisation")
    def __del__(self):
        print("I am doing cleanup activity")
t1=Test()
t2=t1
t3=t2
t4=Test()
t5=t4
print("Deleting t1")
time.sleep(5)
del t1
print("Deleting t2")
time.sleep(5)
del t2
print("Deleting t3")
time.sleep(5)
del t3
print("Deleting t4")
time.sleep(5)
del t4
print("Deleting t5")
time.sleep(5)
del t5
print("End of application")
