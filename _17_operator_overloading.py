# Operator overloading is a feature in python that allow developers to redefine the behavior of mathematical and comparison operators for custom data types. This mean that you can use the standard mathematical operators ( +, -, *, /, etc) and comparision operators ( >, <, ==, etc) in your own classes, just as you would for built-in data types like int, float, and str. 

class Vector:
    def __init__(self,i,j,k) -> None:
        self.i = i 
        self.j = j
        self.k = k
        
    def __str__(self) -> str:
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.i + other.i, self.j + other.j, self.k + other.k)
    
v1 = Vector(3,5,7)
print(v1)

v2 = Vector(1,2,9)
print(v2)

print("Sum")
print(v1 + v2)