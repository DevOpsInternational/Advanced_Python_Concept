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
wish("Mona")
wish("Tejaswita")
wish("Tony")
wish("Mona")
