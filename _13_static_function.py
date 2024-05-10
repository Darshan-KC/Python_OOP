# Trying python static function

class Math:
    def __init__(self,num) -> None:
        self.num = num

    def add_to_num(self,num) -> None:
        self.num +=num

    @staticmethod
    def add(a,b):
        return a + b
    
mth = Math(6)
print(mth.num)

mth.add_to_num(10)
print(mth.num)

print(Math.add(4,6))