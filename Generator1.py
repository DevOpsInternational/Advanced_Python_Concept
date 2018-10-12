#generator use
def my_gen():
    n=100
    print("First type here")
    yield(n)
    n+=1
    print("Second type here")
    yield(n)
for item in my_gen():
    print(item)
