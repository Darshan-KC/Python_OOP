# Instance Vs Class Variable
## Instance
# In python, variable can be defined at the class level or at the instance level. 

## Class Variable
# Class variable are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class.

class Employee:
    # class variable
    companyName = "Dev ell"
    def __init__(self,name) -> None:
        #instance variable
        self.name = name
        self.raise_amount = 0.02
        
    def showDetails(self) -> None:
        print(f"The name of the employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}.")
    

if __name__ == "__main__":  
    emp = Employee("Hari Bahadur")
    emp1 = Employee("Madan Bahadur")
    print(emp.showDetails())

    emp.raise_amount = 0.5
    print(emp.showDetails())

    emp.companyName = "Dev"
    print(emp.showDetails())

    print(emp1.showDetails())

    print(emp.showDetails())

    Employee.companyName = "Ram"
    print(emp.showDetails())
    print(emp1.showDetails())