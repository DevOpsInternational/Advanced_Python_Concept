#use of magic methods
class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
b1=Book(100)
b2=Book(289)
print(b1+b2)
