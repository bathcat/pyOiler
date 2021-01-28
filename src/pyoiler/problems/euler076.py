from typing import Iterable, Tuple, List
from ..shared.solver import Solver
from toolz import pipe,unique,count

#Borrowed from:
#   http://code.activestate.com/recipes/218332-generator-for-integer-partitions/


def partitions(n):
    a = [1]*n
    y = -1
    v = n
    while v > 0:
        v -= 1
        x = a[v] + 1
        while y >= 2 * x:
            a[v] = x
            y -= x
            v += 1
        w = v + 1
        while x <= y:
            a[v] = x
            a[w] = y
            yield a[:w + 1]
            x += 1
            y -= 1
        a[v] = x + y
        y = a[v] - 1
        yield a[:w]



def _solve(print=print):
    n =100
    ps = partitions(n)
    print(f"How many different ways can {n} be written as a sum of at least two positive integers?")
    print(f"Answer: {count(ps)-1}")
    return True


description = '''It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
'''

solver = Solver(76,
                'Counting summations',
                description,
                _solve
                )
