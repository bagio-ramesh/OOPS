from abc import ABC,abstractmethod

class Bike(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Ninja(Bike):

    def start(self):
        print("Ninja Bike Start Method")
        
    def accelerate(self):
        print("Ninja Bike Accelerate Method")

    def stop(self):
        print("Ninja Bike Stop Method")
       
bike_instance = Ninja()
bike_instance.start()
bike_instance.accelerate()
bike_instance.stop()
