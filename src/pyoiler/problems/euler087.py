from ..shared.solver import Solver
from ..shared.primes import primes_below
import math
import itertools

"""[summary]

First naive implementation:
  Answer: 1139575 (Wrong, according to https://projecteuler.info/problem=87)
  Time: 415s
  (I think the problem was that some numbers can be expressed as a 
  triple in multiple ways, so some got counted twice.)

MVP implementation:
  Answer: 1097343 (Correct, says Euler)
  Time: .41s

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
    
    primes = primes_below(math.isqrt(limit))
    
    squares = (p**2 for p in primes)
    cubes = itertools.takewhile(lambda t: t<limit,(p**3 for p in primes))
    h_cubes = itertools.takewhile(lambda t: t<limit,(p**4 for p in primes))

    terms = itertools.product(squares,cubes,h_cubes)

    triples = set()
    for s,c,h in terms:      
        triple = s+c+h
        if triple < limit:
            triples.add(triple)

    print(f'Result (len): {len(triples)}')

    return True





solver = Solver(87,
                "Prime power triples",
                description,
                _solve
                )
