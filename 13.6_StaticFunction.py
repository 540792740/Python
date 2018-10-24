class A(object):
    name = "Cristiano"

    def test1(self):
        print("")

    @classmethod
    # 修饰器,类方法

    def test2(cls):
        cls.name = "Ronaldo"
        print("A's test2 method")

    @staticmethod
    # 静态方法,也是一种类方法，没有默认传递的参数
    def test3():
        A.name = "CR7"
        print("test3 inicializing")

a = A()
a.test2()
a.test3()
# classmethod can change the perameter of the class
print(A.name)
print(a.name)
