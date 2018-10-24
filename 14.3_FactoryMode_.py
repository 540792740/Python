class Person(object):
    def __init__(self, name):
        self.name = name

    def work(self, Axe_type):
        print(self.name + " work begin")

        factory = Steel_Axe_Factory()

        axe = factory.create_axe()
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

class Factory(object):
    def create_axe(self):
        pass

class Stone_Axe_Factory(Factory):
    def create_axe(self):
        return StoneAxe("Granite")
class Steel_Axe_Factory(Factory):
    def create_axe(self):
        return SteelAxe("steel")



p1 = Person("MX")
p1.work("stone")
