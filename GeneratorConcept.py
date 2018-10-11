#use of generator
def countdown(num):
    print("Start Countdown")
    while(num>0):
        yield num#2 1
        print("hi")#3
        num=num-1
values=countdown(10)#2 0
print(values)#1
for x in values:
    print("hello")
    print(x)#4
