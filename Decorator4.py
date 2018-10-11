#decorator chaining
def decor2(fun):#2 i/p is wish function
    def inner(name):
        print("I am executing decor2")
        fun(name)
    return inner#3 returned the inner function
def decor1(fun):#4 decor2's inner function came here
    def inner(name):
        print("I am executing decor1")
        fun(name)
    return inner

@decor2
@decor1
def wish(name):
    print("Your name is: ",name)
wish("Tejaswita")#1
wish("Mona")
wish("Sona")
