class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("This animal is eating!")

    def sleep(self):
        print("This animal is sleeping!")

class Prey(Animal):
    def flee(self):
        print("This animal is fleeing!")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting!")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bunny")
hawk = Hawk("Hawky")
fish = Fish("Fishy")