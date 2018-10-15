#creating zip file
import zipfile as zp
with zp.ZipFile("files.zip","w",zp.ZIP_DEFLATED)as f:
    f.write("FileHandeling.py")
    f.write("FileHandeling1.py")
    f.write("FileHandeling2.py")
    f.write("Generator.py")
    f.write("Generator1.py")
    f.write("Generator2.py")
    f.write("Generator3.py")
    f.write("Generator4.py")
print("files.zip is created successfully")
    
