from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):

    def __init__(self, length, width):

        if length <= 0 or width <= 0:

            raise ValueError("Length and width must be positive!")
        
        self.length = length

        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
shape_num1 = int(input("Enter Area of Rectangle:"))
shape_num2 = int(input("Enter Perimeter of Rectangle:"))


shape_instance=Rectangle(shape_num1,shape_num2)

print("Area:",shape_instance.area())
print("Perimeter:",shape_instance.perimeter())


