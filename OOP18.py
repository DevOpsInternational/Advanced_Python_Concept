#private variable in class
class Test:
    def m1(self):
        self.__x=10
t=Test()
t.m1()
print(t._Test__x)
