# Async IO in Python

# Asynchronous I/O, or async for short, is a programming pattern that allows for high performance I/O operations in a concurrent and non-blocking manner. In python, async programming is achieved through the use of the asyncio module and asynchronous functions.

import asyncio
import time

def function1():
    time.sleep(3)
    print("func 1")
    
def function2():
    time.sleep(3)
    print("func 2")
    
def function3():
    time.sleep(3)
    print("func 3")
    
function1()
function2()
function3()