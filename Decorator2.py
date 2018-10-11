#Use of decorator
def decor(fun):
    def inner(name):
        if name=="Mona":
            print("Hello",name,"How are you?")
        else:
            fun(name)
    return inner

@decor
def wish(name):
    print("Hello",name,"Nice meeting you")
decorfun=decor(wish)#explicit calling decor function,it is returning inner function
decorfun("Mona")
##wish("Mona")
wish("Mona")
wish("Tejaswita")
wish("Tony")
wish("Mona")
