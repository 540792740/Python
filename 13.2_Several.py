class A:
    def test(self):
        print("Come from A")
class B:
    def test(self):
        print("Come from B")
class C(A, B):
    def test1(self):
        print("C")

c = C()
c.test()
print(C.mro())
