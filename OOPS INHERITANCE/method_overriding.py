class Parent:

    def phone(self):
        print("SamsungA51")

    def car(self):
        print("BMW")

class Child(Parent):

    def cycle(self):
        print("BMX")

    def rc_car(self):
        print("EREVO XL")


child_instance = Child()

child_instance.cycle()
child_instance.phone()
child_instance.car()


# 