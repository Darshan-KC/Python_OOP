# Multithreading
# Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process. In Python, we can use the threading module to implement multithreading. In this tutorial, we will take a closer look at the threading module and its various functions and how they can be used in Python. 

# Importing Threading
# We can use threading by importing the threading module.

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

def main():
    time1 = time.perf_counter()

    # func(4)
    # func(4)
    # func(4)

    # time2 = time.perf_counter()
    # print("Tradition time is ",(time2 - time1))


    t1 = threading.Thread(target=func,args=[4])
    t2 = threading.Thread(target=func,args=[4])
    t3 = threading.Thread(target=func,args=[4])

    # This will start the process and move forward
    t1.start()
    t2.start()
    t3.start()

    # This will wait for the process to complete e.g wait for t1 but since the process are already run in parallel. All the process will finish at once.
    t1.join()
    t2.join()
    t3.join()

    time2 = time.perf_counter()
    print("Threading time is ",(time2 - time1))
    
def poolDemo():
    with ThreadPoolExecutor() as executor:
        # future1 = executor.submit(func,4)
        # future2 = executor.submit(func,3)
        # future3 = executor.submit(func,2)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        
        l = [4,3,2]
        results = executor.map(func,l)
        for result in results:
            print(result)

poolDemo()