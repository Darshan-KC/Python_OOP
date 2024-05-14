# A class method is a type of method that is bound to the class and not the instance of the class. In other words, it operates on the class as a whole, rather than on a specific instance of class.
# Class methods are defined using the "@classmethod" decorator, followed by a function definition. The first argument of the function is always "cls", which represents the class.

class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
        
    def changeCompany(cls, newCompany):
        cls.company = newCompany
        
e1 = Employee()
e1.name = "Ram"
e1.show()

e1.changeCompany("KC")
e1.show()

print(Employee.company)