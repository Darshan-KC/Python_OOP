# Encapsulation – Public, Protected, Private members
class MyClass:
    def __init__(self) -> None:
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

class Derived(MyClass):
    pass

obj = MyClass()
print(obj.public)