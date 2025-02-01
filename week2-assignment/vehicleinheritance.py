class Vehicle:
    def move(self):
        print("The vehicle can move")
class Car(Vehicle):
    def drive(self):
        print("The car can move using petrol or diesel or charging")
class Bike(Vehicle):
    def drive(self):
        print("The bike can move using petrol")
class Electric_car(Car):
    def charge(self):
        print("The electric car can move using charging")

e=Electric_car()
e.move()
e.drive()
e.charge()