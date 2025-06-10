class Vehicle:

    def __init__(self,name):

        self.name = name

class Car(Vehicle):

    def __init__(self,name,seat_capacity,fuel_type,engine_model):
        super().__init__(name)
        self.seat_capacity = seat_capacity
        self.fuel_type = fuel_type
        self.engine_model = engine_model

    def display_car(self):
        print(self.name,self.seat_capacity,self.fuel_type,self.engine_model)

car_instance1 = Car("BMW",4,"Petrol","V8")

car_instance1.display_car()

