from abc import ABC,abstractmethod
class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
class Car(IVehicle):
    def start_engine(self):
        print("Car has started")
    def stop_engine(self):
        print("Car has stopped")
class Bike(IVehicle):
    def start_engine(self):
        print("Bike has started")
    def stop_engine(self):
        print("Bike has stopped")
class Truck(IVehicle):
    def start_engine(self):
        print("Truck has started")
    def stop_engine(self):
        print("Trcuk has stopped")
c = Car()
b = Bike()
t = Truck()
c.start_engine()
c.stop_engine()
b.start_engine()
b.stop_engine()
t.start_engine()
t.stop_engine()

        