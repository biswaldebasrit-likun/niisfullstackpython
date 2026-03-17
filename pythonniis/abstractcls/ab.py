from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def perimeter(self):
        return 4 * self.side
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c
s = Square(5)
t = Triangle(3, 4, 5)
print("Perimeter of Square:", s.perimeter())
print("Perimeter of Triangle:", t.perimeter())