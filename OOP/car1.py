class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"The {self.color} {self.model} is driving.")

    def stop(self):
        print(f"The {self.color} {self.model} has stopped.")

    def describe(self):
        sale_status = "for sale" if self.for_sale else "not for sale"
        print(f"{self.year} {self.color} {self.model} is {sale_status}.")


car1 = Car("Toyota Camry", 2020, "Red", True)
car2 = Car("Honda Accord", 2019, "Blue", False)
print(car1.model)  # Output: Toyota Camry
print(car1.year)   # Output: 2020
print(car1.color)  # Output: Red
print(car1.for_sale)  # Output: True 

print(car2.model)  # Output: Honda Accord
print(car2.year)   # Output: 2019

car1.drive()  # Output: The Red Toyota Camry is driving.
car1.stop()   # Output: The Red Toyota Camry has stopped.

car2.describe()  # Output: 2019 Blue Honda Accord is not for sale.