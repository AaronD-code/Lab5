import math

class Shape:
    def area(self):
        raise NotImplementedError("area not implemented")

    def perimeter(self):
        raise NotImplementedError("perimeter not implemented")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


if __name__ == "__main__":
    shapes = [Circle(3), Square(4), Triangle(3, 4, 5)]
    for s in shapes:
        print(type(s).__name__, "area:", s.area(), "perimeter:", s.perimeter())