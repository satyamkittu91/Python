class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, make, model, horse_power, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]

    def display_car(self):
        return f"{self.make} {self.model} with {self.engine.horse_power} HP and {self.wheels[0].size}\" wheels."

my_car = Car("Toyota", "Camry", 200, 16)
print(my_car.display_car())  # Output: Toyota Camry with 200 HP and 16" wheels.
