#string reversal using generator function
def my_gen():
    s=input("Enter a string to reverse")
    l=s.split()
    for i in l[::-1]:
        yield(i)
for item in my_gen():
    print(item,end=" ")
