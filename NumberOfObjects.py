#find number of objects created for class
class Animal:
    legs=4
    @classmethod #compulsary need annotation
    def cat(cls):
        print("Cat has",cls.legs,"legs")

a=Animal()
a.cat()
Animal.cat()
Animal.noofObjects()
