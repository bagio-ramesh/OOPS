class Parent:

    def __init__(self):

        self.vehicles = ["alto","Baleno","Octavia"]

    def get_vehicles(self):

        return self.vehicles
    
class Child(Parent):

    def __init__(self):
        super().__init__()
        self.get_vehicles()

    def get_vehicles(self):
        self.vehicles = super().get_vehicles()

        self.vehicles.append("gWagon")
        self.vehicles.append("BMW")
        return self.vehicles

child_instance = Child()
print(child_instance.vehicles)