#Multithreading programming,getting number of active threads
from threading import *
import time
def sqr(l):
    print("I am doing square: ",current_thread().getName())
    for i in l:
        print("Square of: ",i)
        print(i**2)
def dub(l):
    print("I am doing double: ",current_thread().getName())
    for i in l:
        print("Double of: ",i)
        print(i+i)
l=[1,2,3,4,5]
t1=Thread(target=sqr,args=(l,),name="Tejaswita")
t2=Thread(target=dub,args=(l,),name="Kartiki")
t1.start()
time.sleep(10)
t2.start()
time.sleep(10)
l=enumerate()
for i in l:
    print("Active thread: ",i.name)
print("Number of active threads: ",active_count())
time.sleep(10)
print("Number of active threads: ",active_count())

