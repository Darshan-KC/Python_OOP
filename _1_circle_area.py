#  Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.

import math
class Circle:
    
    def __init__(self,radius) -> None:
        self.radius = radius 
        
    def area(self):
        print("The area of circle is ",math.pi * self.radius * self.radius)
        
    def perimeter(self):
        print("The perimeter of circle is ",2*math.pi*self.radius)
        
obj = Circle(7)
obj.perimeter()
obj.area()