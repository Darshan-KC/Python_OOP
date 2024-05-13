## The dir() method
# dir(): The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object. 

x = [1,2,3]
# e.g. it show what methods i can use with list
print(dir(x))

## The __dict__ attribute
# __dict__ : The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection. 

class Person:
    def __init__(self,name, age) -> None:
        self.name = name
        self.age = age
        
p = Person("Hari",20)
print(p.__dict__)

## The help() method
# help() : The help() function is used to get help documentation for an object, including a description of its attribute and methods.

print(help(Person))