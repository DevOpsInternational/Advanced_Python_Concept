#unzipping zip file
import zipfile as zp
with zp.ZipFile("files.zip","r",zp.ZIP_STORED)as f:
    name=f.namelist()
    for n in name:
        print("File Name is: ",n)
        print("The content of file is: ")
        f1=open(n,"r")
        data=f1.read()
        print(data)
        print()
    
print("files.zip is unzipped successfully")
