import math
import random

cache = {}


def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    # v = math.pow(x, y)
    # v = math.factorial(v)
    # v //= (x + y)
    # v %= 982451653

    if i not in cache:
        cache[i] = x, y

    return cache[i]


def lookup_table():
    for x, y in range(50000):
        slowfun(x, y)


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
