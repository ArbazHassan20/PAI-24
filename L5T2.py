from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Creating instances of each shape
rectangle = Rectangle(5, 4)
triangle = Triangle(9, 6)
square = Square(7)

# Printing the area of each shape
print(f"Area of Rectangle: {rectangle.area()}")
print(f"Area of Triangle: {triangle.area()}")
print(f"Area of Square: {square.area()}")
