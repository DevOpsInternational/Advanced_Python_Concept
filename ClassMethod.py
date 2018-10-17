#use of class method
class Animal:
    legs=4
    @classmethod
    def cat(cls):
        print("Cat has",cls.legs,"legs")

a=Animal()
a.cat()
Animal.cat()
