#unpickling
import pf
from pickle import *
f=open("pf.dat","rb")
print("Employee Details are")
while True:
    try:
        obj=load(f)
        obj.disp()
        print()
    except EOFError:
        print("All Employees Completed")
        break
f.close()
