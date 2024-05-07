# Trying map filter and reduce
from functools import reduce

# Map
def cube(n):
    return n**3

lst = [1,2,3,4]
print(list(map(cube,lst)))

# Filter
def filter_function(a):
    return a>2

newl = list(filter(filter_function,lst))
print(newl)

# Reduce

# sum = reduce(lambda x,y: x + y, lst)

def mysum(x,y):
    return x+y 

sum = reduce(mysum,lst)
print(sum)