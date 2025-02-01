from abc import ABC,abstractmethod
class Icalculator(ABC):
    @abstractmethod
    def add(self):
        pass
    def subtract(self):
        pass
    def multiply(self):
        pass
    def divide(self):
        pass
class Basiccalculator(Icalculator):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("Addition:",self.a+self.b)
    def subtract(self):
        print("Subtraction:",self.a-self.b)
    def multiply(self):
        print("Multiplication:",self.a*self.b)
    def divide(self):
        print("Division:",self.a/self.b)
c=Basiccalculator(4,8)
c.add()
c.subtract()
c.multiply()
c.divide()    
        
    