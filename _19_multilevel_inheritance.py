# Multilevel inheritance is a type of inheritance in object-oriented programming where a derived class inherits from another derived class. This type of inheritance allow you to build a hierarchy of classes where one class builds upon another, leading to more specialized class. 

class Animal:
    def __init__(self,name, species) -> None:
        self.name = name
        self.species = species
        
    def showDetails(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")
        
class Dog(Animal):
    def __init__(self, name, breed) -> None:
        # super().__init__(name, species)
        Animal.__init__(self,name, species="Dog")
        self.breed = breed
        
    def showDetails(self):
        # return super().showDetails()
        Animal.showDetails(self)
        print(f"Breed : {self.breed}")
        
class GoldenRetriever(Dog):
    def __init__(self, name, color) -> None:
        # super().__init__(name, breed)
        Dog.__init__(self,name, breed="Golden Retriever")
        self.color = color
        
    def showDetails(self):
        # return super().showDetails()
        Dog.showDetails(self)
        print(f"Color : {self.color}")
        
o = GoldenRetriever("Tom","Blue")
o.showDetails()
print(GoldenRetriever.mro())