# Write a Python program to create a calculator class. Include methods for basic arithmetic operations.
class Calculator:
    def __init__(self,num1,num2) -> None:
        self.num1 = num1
        self.num2 = num2
        
    def sum(self):
        print("The sum of {} and {} is {}".format(self.num1,self.num2, (self.num1 + self.num2)))
    
    def difference(self):
        print("The difference of {} from {} is {}".format(self.num1,self.num2, (self.num1 - self.num2))) 
    
    def product(self):
        print("The product of {} and {} is {}".format(self.num1,self.num2, (self.num1 * self.num2))) 
    
    def divison(self):
        print("The division of {} and {} is {}".format(self.num1,self.num2, (self.num1 / self.num2)))
    
    def remainder(self):
        print("The remainder {} and {} is {}".format(self.num1,self.num2, (self.num1 % self.num2))) 


def numcheck(num)->eval:
    try:
        n = eval(num)
    except:
        print("Invalid type")
        tem = input("Enter the valid number: ")
        n = numcheck(tem)
    
    return n
    
num1 = input("Enter the first number: ")
num1 = numcheck(num1)
num2 = input("Enter the second number: ")
num2 = numcheck(num2)
op = input("Enter the operator: ")

while(not((op == "+") or (op == "-") or (op == '*') or (op == '/') or (op == '%'))):
    print("The operator is ", op)
    print("\n!!!\tThe operator must be one of ('+','-','*','/','%')!!!")
    op = input("Enter the correct operator: ")

cal = Calculator(num1,num2)
if(op == '+'):
    cal.sum()
elif op == '-':
    cal.difference()
elif op == '*':
    cal.product()
elif op == '/':
    cal.divison()
else:
    cal.remainder()