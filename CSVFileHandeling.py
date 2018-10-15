#writing data to csv file
import csv
with open("emp.csv","w") as f:
    w=csv.writer(f)
    w.writerow(["EmployeeName","EmployeAddress" ])
    n=int(input("Enter number of Employees"))
    for i in range(n):
        ename=input("Enter the name of employee")
        eadd=input("Enter the employee address")
        w.writerow([ename,eadd])
print("Data entered of {} number of employees".format(n))
