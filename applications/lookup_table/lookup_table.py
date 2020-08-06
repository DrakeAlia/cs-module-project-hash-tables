# Your code here
import random
import math 
lookup_table = {}

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
    
    # We can use cacheing to avoid doing repeated calculations 
    # We will fill the lookuptable with results and return them when they are called
    # If x & y are not in the lookup table then run the old code
    if (x, y) not in lookup_table:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653
        # Set lookup table with the variables to v
        lookup_table[(x, y)] = v

    return lookup_table[(x, y)]



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
