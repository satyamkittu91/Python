from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("The car is moving!")

    def stop(self):
        print("The car has stopped!")

class Bike(Vehicle):
    def go(self):
        print("The bike is moving!")

    def stop(self):
        print("The bike has stopped!")

class boat(Vehicle):
    def go(self):
        print("The boat is sailing!")

    def stop(self):
        print("The boat is anchoring!")