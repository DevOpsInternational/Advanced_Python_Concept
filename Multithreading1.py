#Multithreading programming
from threading import *
def sqr(l):
    print("I am doing square")
    for i in l:
        print("Square of: ",i)
        print(i**2)
def dub(l):
    print("I am doing double")
    for i in l:
        print("Double of: ",i)
        print(i+i)
l=[1,2,3,4,5]
t1=Thread(target=sqr,args=(l,))
t2=Thread(target=dub,args=(l,))
t1.start()
t2.start()
