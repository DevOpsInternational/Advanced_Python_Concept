#string reversal using generator function
def my_gen():
    s=input("Enter a string to reverse")
    for i in range(len(s)-1,-1,-1):
        yield(s[i])
for item in my_gen():
    print(item,end="")
