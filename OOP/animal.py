class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")
    
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says: Woof!")


dog1 = Dog("Buddy")
dog1.eat()
dog1.sleep()
dog1.bark()