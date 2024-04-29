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
    def __init__(self,base,height,side1,side2,side3) -> None:
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3 
        
    def area(self)->float:
        return 1/2*self.base * self.height
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    

circle = Circle(7)
print(f"The perimeter of circle is {circle.perimeter():.3f}")
print(f"The area of circle is {circle.area():.3f}")