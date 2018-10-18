#inheritance
class X:
    a=10
    def __init__(self):
        print("I am parent class constructor")
    @classmethod
    def m1(cls):
        print("I am classmethod")
    def m2(self):
        print("I am parent class instance method")
    @staticmethod
    def stat():
        print("I am parent class static method")
class Y(X):
    pass
y=Y()
print(y.a)
y.m1()
y.m2()
y.stat()
