#Smart division using decorator
def smartdiv(fun):
    def s(a,b):
        if b==0:
            print("Please change your second number,\
because can't divide by Zero")
        else:
            fun(a,b)
    return s
@smartdiv
def normalDiv(a,b):
    print("Division of two numbers is: ",a/b)
normalDiv(9,2)
normalDiv(10,3)
normalDiv(9,0)
normalDiv(10,0)
