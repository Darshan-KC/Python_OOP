# Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like circle, triangle, and square.
from math import pi
class Shape:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self,radius) -> None:
        self.radius = radius
    
    def area(self)->float:
        return pi*self.radius**2
    
    def perimeter(self) ->float:
        return 2*pi*self.radius
    
class Triangle(Shape):
    def __init__(self,base,height,side1,side2) -> None:
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        
    def area(self)->float:
        return 1/2*self.base * self.height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.base
    
class Square(Shape):
    def __init__(self,length) -> None:
        self.length = length
        
    def perimeter(self):
        return 4*self.length
    
    def area(self)->float:
        return (self.length**2)

circle = Circle(7)
print(f"The perimeter of circle is {circle.perimeter():.3f}")
print(f"The area of circle is {circle.area():.3f}")

triangle = Triangle(8,5,6,6)
print(f"The perimeter of triangle is {triangle.perimeter():.3f}")
print(f"The area of triangle is {triangle.area():.3f}")

square = Square(5)
print(f"The perimeter of square is {square.perimeter():.3f}")
print(f"The area of square is {square.area():.3f}")