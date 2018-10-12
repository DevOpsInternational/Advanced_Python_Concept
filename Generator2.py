#use of generator with for loop
def mygen():
    yield("A")
    yield("B")
    yield("C")
    yield("D")
    yield("E")
    yield("F")

for i in mygen():
    print(i)
