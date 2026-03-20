# Duck Typing

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Car:
    alive = False
    def speak(self):
        print("Beep!")

    
animals = [Dog(), Cat(), Dog()]
for animal in animals:
    animal.speak()
    print(animal.alive)  # Output: True for all animals