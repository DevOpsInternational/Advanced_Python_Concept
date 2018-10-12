#program to generate six digit OTP
from random import*
for i in range(0,11):
    print(randint(0,9),randint(0,9),randint(0,9),\
          randint(0,9),randint(0,9),randint(0,9),sep=" ")
