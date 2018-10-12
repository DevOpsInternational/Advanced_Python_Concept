#generator use
def my_gen():
    n=100
    print("First type here")
    yield(n)
    n+=1
    print("Second type here")
    yield(n)
a=my_gen()
print(next(a))
print(next(a))
