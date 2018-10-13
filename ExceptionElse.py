#Exception with else block
#else block is executed only when there is no exception in try block
try:
    print("I am try block,No exception occured")
except:
    print("I am except block executed when there is exception in try block")
else:
    print("I am else block,executed when there is no exception in try block")
finally:
    print("I am finally block I get executed everytime")
