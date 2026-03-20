class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        #print(f"A {self.color} {self.__class__.__name__.lower()} that is {"filled" if self.filled else "not filled"}.")
        print(f"A {self.color} shape that is {'filled' if self.filled else 'not filled'}.")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled) # Using constructor of parent class
        self.radius = radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius ** 2}")
        super().describe() # Calling the describe method of the parent class

class Square(Shape):
    def __init__(self, color, filled, side_length):
        super().__init__(color, filled)
        self.side_length = side_length

    def describe(self):
        print(f"It is a square with an area of {self.side_length ** 2}")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, filled, base, height):
        super().__init__(color, filled)
        self.base = base
        self.height = height

    def describe(self):
        print(f"It is a triangle with an area of {0.5 * self.base * self.height}")
        super().describe()


circle = Circle("red", True, 5)
square = Square("blue", False, 4)
triangle = Triangle("green", True, 3, 4)

square.describe()  # Output: A red shape that is filled.