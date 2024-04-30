# Using the super() function. Define a base class Animal and derived class Dog 
class Animal:
    def __init__(self,name) -> None:
        self.name = name
        
    def speak(ram)-> str: 
        return f"{ram.name} say hello"
    
class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
        
    def speak(self) -> str:
        return f"{self.name} barks"
    
ram = Animal("Ram")
print(ram.speak())

dog = Dog("Lucy")
print(dog.speak())