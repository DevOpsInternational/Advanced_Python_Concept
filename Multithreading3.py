#Multithreading programming,giving names to threads
from threading import *
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
t2.start()
