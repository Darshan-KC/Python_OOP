# Multiple inheritance is a powerful feature in object-oriented programming that allows a class to inherit attributes and methods from multiple parent classes. This can be useful in situations where a class needs to inherit functionality from multiple sources.

class Employee:
    def __init__(self,name) -> None:
        self.name = name
        
    def show(self):
        print(f"The name is {self.name}")
        
        
class Dancer:
    def __init__(self,dance) -> None:
        self.dance = dance
        
    def show(self):
        print(f"The name is {self.name}")

class DancerEmployee(Employee, Dancer):
    def __init__(self,dance, name) -> None:
        self.name = name
        self.dance = dance
        # super().__init__(name)
        
o = DancerEmployee("Ram","Hari")
print(o.name)
print(o.dance)
o.show()
print(DancerEmployee.mro())