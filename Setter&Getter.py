#use of getter and setter method
class Student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
n=int(input("Enter number of students"))
for i in range(n):
    s=Student()
    name=input("Enter the name of the student")
    s.setName(name)
    marks=input("Enter marks of the student")
    s.setMarks(marks)
    print("Name of the student is: ",s.getName())
    print("Marks of the student are: ",s.getMarks())
