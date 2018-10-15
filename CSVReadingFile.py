#reading data to csv file
import csv
with open("emp.csv","r") as f:
    r=csv.reader(f)
    data=list(r)
    print(type(data))
##    print("EmpName","\t","EmpEdd")
    for i in data:
        for j in i:
            print(j,"\t",end="")
        print()
            
#print("Data entered of {} number of employees".format(n))
k
