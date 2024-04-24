#  Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
class Circle:
    
    def __init__(self,radius) -> None:
        self.radius = radius 
        
    def area(self):
        print("The area of circle is {0}",self.radius * self.radius)
        
    