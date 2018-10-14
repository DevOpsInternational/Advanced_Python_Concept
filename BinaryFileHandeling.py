#binary file handeling
with open("Image.jpg","rb")as f1:
    bytes=f1.read()
##    print(bytes)
with open("Image1.jpg","wb")as f2:
    f2.write(bytes)
