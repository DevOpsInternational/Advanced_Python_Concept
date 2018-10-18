#use of destructor
import time
class Test:
    def __init__(self):
        print("I am doing initialisation")
    def __del__(self):
        print("I am doing cleanup activity")
t=Test()
t=None

time.sleep(20)
print("End of application")
