from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def calculate_area(self):
        print(f"Area of square with {self.radius} is: {3.14*self.radius*self.radius}")
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_area(self):
        print(f"Area of triangle with {self.length}, {self.width} is {self.length*self.width}")
        
s=Circle(4)
s.calculate_area()
r=Rectangle(3,6)
r.calculate_area()