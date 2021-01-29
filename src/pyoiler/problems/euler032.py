from ..shared.solver import Solver
from typing import Iterable 
from sympy.ntheory.digits import digits as s_digits

def get_digits(n:int)->Iterable[int]:
    return s_digits(n)[1:]

def is_pandigital(n:int)->bool:
    ds = get_digits(n)
    ds_s = set(ds)
    return len(ds)==len(ds_s) \
            and \
           max(ds_s)==len(ds)


def _solve(print = print):
    print(f'Not done')
    return False


description = '''
We shall say that an n-digit number is pandigital if it makes use of all 
the digits 1 to n exactly once; for example, the 5-digit number, 15234, 
is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing 
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product 
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to 
only include it once in your sum.
'''

solver = Solver(32,
                'Pandigital products',
                description,
                _solve
                )
