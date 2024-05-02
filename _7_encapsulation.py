# Encapsulation – Public, Protected, Private members
class MyClass:
    def __init__(self) -> None:
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

class Derived(MyClass):
    pass
print("\nBase class\n")
obj = MyClass()
print(obj.public)
print(obj._protected)

# This cannot be access
# print(obj.__private)
print("\n\nDerived class \n")
der = Derived()
print(der.public)
print(der._protected)