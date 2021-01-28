import rx
import math
from rx import operators as ops
from itertools import combinations_with_replacement

from ..shared.solver import Solver

def triplets():
    for a,b in combinations_with_replacement(range(1, 400),2):
        c = math.sqrt(a**2 + b**2)
        if c.is_integer():
            yield a,b,c


def _solve(print=print):
    for a,b,c in triplets():
        if a+b+c == 1000:
            print(str((a, b, c)))
            return True

    return False

description = '''A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
   a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

solver = Solver(9,
                'Special Pythagorean triplet',
                description,
                _solve
                )