from ..shared.solver import Solver
from ..shared.digits import to_big_end_digits as digits
from itertools import count
from ..shared.more_itertools import take

def c_digits():
    for i in count(1):
        yield from digits(i)

def _solve(print = print):
    places = [10**i for i in range(6+1)]
    ds = list(take(max(places) + 2,c_digits()))
    product = 1
    for p in places:
        d = ds[p-1]
        print(f"p:{p} d:{d}")
        product *= d

    print(f"The product of those things is: {product}")
    return True


description = '''An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d[n] represents the nth digit of the fractional part, find the value of the following expression.

d[1] × d[10] × d[100] × d[1000] × d[10000] × d[100000] × d[1000000]

'''

solver = Solver(40,
                "Champernowne's constant",
                description,
                _solve
                )
