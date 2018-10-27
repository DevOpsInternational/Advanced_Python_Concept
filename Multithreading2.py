#Multithreading programming thread identification number
from threading import *
print("Main thread identification number is: ",current_thread().ident)
def sqr(l):
    print("This child thread identification number is: ",current_thread().ident)
    print("I am doing square")
    for i in l:
        print("Square of: ",i)
        print(i**2)
def dub(l):
    print("This child thred identification number is: ",current_thread().ident)
    print("I am doing double")
    for i in l:
        print("Double of: ",i)
        print(i+i)
l=[1,2,3,4,5]
t1=Thread(target=sqr,args=(l,))
t2=Thread(target=dub,args=(l,))
t1.start()
t2.start()
