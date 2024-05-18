# Hybrid inheritance is a combination of multiple inheritance and single inheritance in object oriented programming. It is a type of inheritance in which multiple inheritance is used to inherit the properties of multiple base classes into a single derived class, and single inheritance is used to inherit the properties of derived class into a sub-derived class.

# In python, hybrid inheritance can be implement by creating a class hierarchy, in which a base class is inherited by multiple derived classes, and one of the derived classes is further inherited by a sub-derived class.

class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(Derived1,Derived2):
    pass