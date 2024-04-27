# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def __init__(self,num1,num2) -> None:
        self.num1 = num1
        self.num2 = num2
        
    def sum(self):
        return self.num1 + self.num2
    
    def difference(self):
        return self.num1 - self.num2 
    
    def product(self):
        return self.num1 * self.num2 
    
    def divison(self):
        return self.num1 / self.num2
    
    def remainder(self):
        return self.num1 % self.num2 
    
    