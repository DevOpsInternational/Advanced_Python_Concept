#working with random module
#generate random floating point number between 0 and 1 excluding 0,1
from random import *
for i in range(0,11):
    print(random())
#when i want to generate integer value
for i in range(0,11):
    print(randint(1,100),end=" ")
#returns random number between range
print()
for i in range(0,11):
    print(randrange(1,100,5),end=" ")
print()
#use of choice function
l=["Sunny","Rainy","Cloudy","Overcast","Rain","Humid"]
for i in range(0,11):
    print(choice(l),end=" ")
