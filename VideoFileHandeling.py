#binary file handeling for video files
with open("Video1.mp4","rb")as f1:
    bytes=f1.read()
##    print(bytes)
with open("Video2.mp4","wb")as f2:
    f2.write(bytes)
