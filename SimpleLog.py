#sending exception information to logging file
import logging as lg
lg.basicConfig(filename="Logging19.txt",level=lg.DEBUG)
lg.info("New request came,we welcome you")
try:
    a=int(input("Enter value of one number"))
    b=int(input("Enter value of another number"))
    print(a/b)
except ZeroDivisionError as msg:
    print("You cannot divide number with zero")
    lg.exception(msg)
except ValueError as msg:
    print("Enter proper value of numbers")
    lg.exception(msg)
lg.info("Request of mathematical calculation in processed")
