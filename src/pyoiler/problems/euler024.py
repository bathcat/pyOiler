import itertools
from ..shared.more_itertools import nth
from ..shared.solver import Solver
from ..shared.digits import from_digits

def _solve(print=print):
    all_digits = list(range(0,10))
    permutations = itertools.permutations(all_digits)
    digits = nth(permutations, 100)
    n = from_digits(digits)
    print('The millionth permutation is: ' + str(n))
    return True

description = '''A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

solver = Solver(24,
                'Lexicographic permutations',
                description,
                _solve
                )