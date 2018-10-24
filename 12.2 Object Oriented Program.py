class Car:
    def start(self):
        print("I am a car")
    def print_car_inf(self):
        print("Color is %s, Name is %s" %(self.color, self.name))

c = Car()
c.name = "Mikun"
c.color = "Red"
c.print_car_inf()
c.start()


class Person():
    # magic method : "__xxx__"
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def introduce(self):
        print("name is :%s, age is :%s"%(self.name, self.age))

    # translate into String.
    def __str__(self):
        return "name is :%s, age is :%s"%(self.name, self.age)

p1 = Person("Zhang San", 18, 1.80)
# p1.introduce()
print(p1)


