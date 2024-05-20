# Time module

# The time module in python provides a set of functions to work with time related operations, such as timekeeping, formatting, and time conversions.

# time.time()
#The time.time() function returns the current time as a floating point number, representing the number of seconds since the epoch (the point in time when the time module was initialized). The returned value is based on the computer's system clock and is affected by time adjustments made by the operating system, such as daylight saving time.

import time

print(time.time())
init = time.time()

print("Before sleep")
time.sleep(2)
print("This is printed after 2 second")

t = time.localtime()
print("Time is ",time.strftime("%H:%M:%S",t))

