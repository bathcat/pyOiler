from ..shared.solver import Solver
from ..shared.primes import primes_below
import math
from sympy.utilities.iterables import variations


"""[summary]

First naive implementation:
  Answer: 1139575 (Wrong, according to https://projecteuler.info/problem=87)
  Time: 415s

"""

description = '''
The smallest number expressible as the sum of a prime square, prime cube, 
and prime fourth power is 28. In fact, there are exactly four numbers 
below fifty that can be expressed in such a way:

28 = 2**2 + 2**3 + 2**4
33 = 3**2 + 2**3 + 2**4
49 = 5**2 + 2**3 + 2**4
47 = 2**2 + 3**3 + 2**4

How many numbers below fifty million can be expressed as the sum of a 
prime square, prime cube, and prime fourth power?
'''

def _solve(print = print):
    limit = 50_000_000
    ps = primes_below(math.isqrt(limit))

    n_count = 0
    for a,b,c in variations(ps,3,True):      
        n_0 = a**2
        n_1 = n_0+ b**3
        if n_1>=limit:
            continue
        n = n_1 + c**4
        if n < limit:
            n_count+=1

    print(f'Result (n_count): {n_count}')

    return False





solver = Solver(87,
                "Prime power triples",
                description,
                _solve
                )
