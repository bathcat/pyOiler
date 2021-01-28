from ..shared.list_arithmatic import add
from ..shared.digits import to_digits
from itertools import permutations
from ..shared.solver import Solver


def digit_sum(n:int)->int:
    return add(to_digits(n))

def digit_sums(biggest: int):
    pool = list(range(0,biggest))
    for a, b in permutations(pool,2):
        power = a**b
        yield a, b, power, digit_sum(power)


def _solve(print=print):
    biggest = max(digit_sums(100), key=lambda x: x[3])
    print(f"{biggest[0]}**{biggest[1]}=={biggest[2]}")
    print(f"Digit sum: {biggest[3]}")
    return True

description = '''A googol (10**100) is a massive number: one followed by one-hundred zeros; 100**100 is almost 
unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a, b < 100, what is the maximum digital sum?
'''

solver = Solver(56,
                'Powerful digit sum',
                description,
                _solve
                )