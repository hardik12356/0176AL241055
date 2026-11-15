class Shape:
    def display(self):
        print("This is a shape")

class Circle(Shape):
    def area(self, r):
        print("Circle Area:", 3.14 * r * r)

class Rectangle(Shape):
    def area(self, l, b):
        print("Rectangle Area:", l * b)

class Triangle(Shape):
    def area(self, b, h):
        print("Triangle Area:", 0.5 * b * h)

c = Circle()
c.display()
c.area(5)

r = Rectangle()
r.display()
r.area(4, 6)

t = Triangle()
t.display()
t.area(5, 8)