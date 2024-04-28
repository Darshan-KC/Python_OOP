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
    

circle = Circle(7)
print(f"The perimeter of circle is {circle.perimeter():.3f}")
print(f"The area of circle is {circle.area():.3f}")