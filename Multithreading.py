#Creating thread using any class
from threading import*
import time
print(current_thread().getName())
def disp():
    print("I am display function executed by thread")
    print(current_thread().getName())
##t=Thread(target=disp)#thread is created
t=Thread(target=disp).start() #this is also valid
##t.start()#thread is started
time.sleep(5)
print(current_thread().getName())
