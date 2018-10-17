#inner and outer class
class Outer:
    def m1(self):
        print("I am outer class")
    class Inner:
        def m2(self):
            print("I am inner class")
Outer().m1()
Outer().Inner().m2()
