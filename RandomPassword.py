#random password of six length contains digits and alphabets
from random import*
for i in range(11):
    print(chr(randint(65,90)and randint(97,122)),randint(0,9),\
          chr(randint(65,90)and randint(97,122)),randint(0,9),\
          chr(randint(65,90)and randint(97,122)),randint(0,9),sep="")
