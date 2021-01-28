from ..shared.digits import to_digits
import itertools
from ..shared.solver import Solver

max_inclusive=6

def have_same_digits(left: int, right: int) -> bool:
    lefts = to_digits(left)
    rights = to_digits(right)
    return set(lefts) == set(rights)

def hits_target(n:int)->bool:
    digits = set(to_digits(n))
    for i in range(2, max_inclusive + 1):
        multiple = n * i
        if not (set(to_digits(multiple)) == digits):
            return False
    return True

def get_thing():
    for i in itertools.count(1):
        if hits_target(i):
            return i

def _solve(print=print):
    target = get_thing()
    print('here''s the number:' + str(target))
    for i in range(1,max_inclusive +1):
        print('n x ' + str(i) + ' = ' + str(target * i))
    return True

description = '''It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

solver = Solver(52,
                'Permuted multiples',
                description,
                _solve
                )
