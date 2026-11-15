from geometry import circle, rectangle

r = float(input("Enter radius: "))

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))

print("Circle Area:", circle.area(r))
print("Circle Circumference:", circle.circumference(r))

print("Rectangle Area:", rectangle.area(l, b))
print("Rectangle Perimeter:", rectangle.perimeter(l, b))