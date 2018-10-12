def f1():
    if __name__=="__main__":
        print("The code is executed directly as program")
        print("The value of name is: ",__name__)
    else:
        print("The code is executed in other program as a module")
        print("The value of name is: ",__name__)
f1()
