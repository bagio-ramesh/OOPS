class Shape:

    def __init__(self,name,color):

        self.name=name

        self.color = color

class Circle(Shape):

    def __init__(self,name,color,radius):

        super().__init__(name,color)

        self.radius = radius
    
    def area(self):
        print(f"area of {self.name} with {self.color} = {3.14*self.radius**2}")


class Rectangle(Shape):
    def __init__(self, name, color, length, width):
        super().__init__(name, color)
        self.length = length
        self.width = width
    
    def area(self):
        print(f"Area of {self.name} {self.color}: = {self.length*self.width}")

    
circle_instance1 = Circle("Circle","Red",10)

circle_instance1.area()


rectangle_instance1=Rectangle("Rectangle","Blue",23,4)
rectangle_instance1.area()

    