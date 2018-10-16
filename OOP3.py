#use of constructor and instance method
class Test:
    def __init__(self):
        print("I am executing constructor")
    def m1(self):
        print("I am instance method in class")
t=Test()
t.m1()
