import os 
with open("fwrite.txt","a+") as f:
    print(f.tell())
    print(f.read(10))
    print(f.tell())
    f.seek(30)
    print("The current position of pointer is: ",f.tell())
    f.write("I am here in middle")
    print("The current position of the pointer is: ",f.tell())
print(os.path.isfile("Generator.py"))
lcount=wcount=ccount=0
with open("Generator.py","r") as f:
    for line in f:
        lcount+=1
        ccount+=len(line)
        words=line.split()
        wcount+=len(words)
print(lcount)
print(wcount)
print(ccount)
        
