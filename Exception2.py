#Programmer defined exceptions
class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg=arg
class TooOldException(Exception):
    def __init__self(self,arg):
        self.msg=arg
age=int(input("Enter your age"))
if age<18:
    raise TooYoungException("Please wait")
elif age>60:
    raise TooOldException("You can't register")
else:
    print("Thanks for registration")
