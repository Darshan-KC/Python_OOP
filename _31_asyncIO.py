# Async IO in Python

# Asynchronous I/O, or async for short, is a programming pattern that allows for high performance I/O operations in a concurrent and non-blocking manner. In python, async programming is achieved through the use of the asyncio module and asynchronous functions.

import asyncio
import time

# def function1():
async def function1():
    # time.sleep(1)
    await asyncio.sleep(1)
    print("func 1")
    
# def function2():
async def function2():
    # time.sleep(1)
    await asyncio.sleep(1)
    print("func 2")
    return "this is function 2"
    
# def function3():
async def function3():
    # time.sleep(1)
    await asyncio.sleep(3)
    print("func 3")
    
async def main():
    # task = asyncio.create_task(function1())
    # await function1()
    # await function2()
    # await function3()
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)
    
asyncio.run(main())
# function1()
# function2()
# function3()