#MRO in python
class P1:pass
class P2:pass
class C(P1,P2):pass
print(C.mro())
print(P1.mro())
