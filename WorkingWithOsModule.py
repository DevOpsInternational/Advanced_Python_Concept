#Working with directory
import os
cwd=os.getcwd()
print("Current working direcotry is: ",cwd)
cwd=os.mkdir("UseMkdir2")
print("New directory created")
cwd=os.mkdir("UseMkdir3/SubDir/SubSubDir")
print("Subdirectory Created")
