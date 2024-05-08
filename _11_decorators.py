# Decorators in python are a powerful and versatile tool that allow you to modify the behaviour or a function and method. They are way to extend the functionlity of a function or method without modifying its source code.

# A decorator  is a function that takes another function as an argument and returns a new function that modifies the behaviour of the original function. 
# The new function is often referred to as a decorated function. The basic syntax for using a decorator is the following: 

def greet(fx):
    def mfx(*args,**kargs): # fx => function, mfx => modified function
        print("Namaste ")
        fx(*args, **kargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("Hello world")
    
@greet
def add(a,b):
    print(a+b)
    
greet(hello())

greet(add(2,4))


# In this example, the greet decorator takes a function as an argument and returns a new function that logs the function call before and after the original function is called.