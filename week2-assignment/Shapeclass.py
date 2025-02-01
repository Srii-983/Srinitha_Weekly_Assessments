class Shape:
    def area(self):
        print('The area is calculated based upon shape')
class Square:
    def __init__(self,side):
        self.side=side
    def area(self):
        print(f"Area of square with {self.side} is: {self.side*self.side}")
class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        print(f"Area of triangle with {self.base}, {self.height} is {0.5*self.base*self.height}")
o=Triangle(4,8)
o.area()
o2=Square(5)
o2.area()
   