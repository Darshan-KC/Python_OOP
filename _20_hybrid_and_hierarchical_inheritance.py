# Hybrid inheritance is a combination of multiple inheritance and single inheritance in object oriented programming. It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class, and single inheritance is used to inherit the properties of derived class into a sub-derived class.

# In python, hybrid inheritance can be implement by creating a class hierarchy, in which a base class is inherited by multiple derived classes, and one of the derived classes is further inherited by a sub-derived class.

class Base1:
    def fun_base1(self):
        print("This is base1")


class Derived1(Base1):
    def fun_Derived1(self):
        print("This is Derived1")

class Derived2(Base1):
    def fun_Derived2(self):
        print("This is Derived2")

class Derived3(Derived1,Derived2):
    def fun_Derived3(self):
        print("This is Derived3")
        
de3 = Derived3()
de3.fun_Derived3()

de3.fun_base1()

print(Derived3.mro())