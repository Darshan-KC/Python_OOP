# The Walrus Operator is a new addition to Python 3.8 and allows you to assign a value to a variable within a expression. This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation. 
# The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements.

a = True
print(a:=False)

# Walrus operator in while loop

numbers = [1,2,3,4,5]

while(n:= len(numbers) > 0):
    print(numbers.pop())
    
# Another example of Walrus operator in if statement

names = ["John","Jane","Jim"]

if(name:= input("Enter a name: ")) in names:
    print(f"Namaste, {name}")
else:
    print("Name not found")
    
     