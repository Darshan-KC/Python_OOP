# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
import datetime

class Person:
    def __init__(self,name,country,dob) -> None:
        self.name = name
        self.country = country
        self.dob = dob 
    
    def date_of_birth(self):
        dob = datetime.datetime.strptime(self.dob,"%Y/%m/%d")
        current_date = datetime.datetime.now()
        age = current_date.year - dob.year
        print("Age of a {} is {}".format(self.name,age))
        
obj = Person("Hari","Nepal","2000/01/01")
obj.date_of_birth()
    