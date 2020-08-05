# Your code here
import random
import math 

lookuptable = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    
    if (x, y) not in lookuptable:
        lookuptable[(x,y)] = slowfun_too_slow(x, y)

    return lookuptable[(x,y)]




# Do it the same way as expensive sequence to optimize
# def slowfun_inner(x, y):
#     v = math.pow(x, y)
#     if v not in cache:
#         cache[v] = math.factorial(v)
#         cache[v] = math.pow(x, y)
#         cache[v] //= x + y
#         cache[v] %= 982451653
#         v = cache[v]

#         return v

#     return slowfun_inner(x, y)


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
