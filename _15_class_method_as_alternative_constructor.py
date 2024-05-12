# A class method belongs to class rather than to an instance of the class. One common use case of class method as alternative constructors is when you want to create an object from that is stored in a different format, such as a string or a dictionary.

class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name 
        self.salary = salary 

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0],int(string.split("-")[1]))
    
e1 = Employee("Harry", 12000)
print(e1.name)
print(e1.salary)

string = "John-12000"
e2 = Employee.fromStr(string)
print(e2.name)  
        