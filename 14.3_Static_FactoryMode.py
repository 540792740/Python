class Person(object):
    def __init__(self, name):
        self.name = name

    def work(self, Axe_type):
        print(self.name + " work begin")

        axe = Factory.create_axe(Axe_type)
        axe.cut_tree()


        # axe = StoneAxe("Granite")
        # axe = SteelAxe("Stelling")
        # axe.cut_tree()

class Axe(object):
    def __init__(self,name):
        self.name = name

    def cut_tree(self):
        print("%s begin to cut"%self.name)

class StoneAxe(Axe):
    def cut_tree(self):
        print("Use Stone Axr")

class SteelAxe(Axe):
    def cut_tree(self):
        print("Use steel Axe")

# 第三方工厂类
# 静态工厂 
class Factory(object):
    @staticmethod

    def create_axe(type):
        if type == "stone":
            return StoneAxe("Geranite")
        elif type == "steel":
            return SteelAxe("Steel")
        else:
            print()


p1 = Person("MX")
p1.work("stone")
p1.work('steel')