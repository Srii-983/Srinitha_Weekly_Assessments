class Car:
    def move(self):
        print("It can move on the road")
class Airplane:
    def move(self):
        print("Airplance can fly in the air")
class Flying_car(Car,Airplane):
    def move(self):
        print("Flying car can move on the road and also can fly in the air")
o1=Flying_car()
o1.move()
        