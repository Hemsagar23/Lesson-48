import math

class Polygon:
    def area(self):
        raise NotImplementedError("Subclass must implement this method")

class Rectangle(Polygon):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Triangle(Polygon):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Polygon):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [
    Rectangle(5, 10),
    Triangle(6, 8),
    Circle(7),
    Square(4)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.area():.2f}")
