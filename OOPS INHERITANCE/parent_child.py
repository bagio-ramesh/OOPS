class Parent:

    def car(self):
        print("BMW")

    def bike(self):
        print("DUCATI H950")


class Child(Parent):  #Inheritance allows child class to inherit the properties and methods of parent class
    def cycle(self):
        print("BMX")


child_instance1 = Child()

child_instance1.car()
child_instance1.bike()
child_instance1.cycle()