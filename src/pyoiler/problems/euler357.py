from ..shared.primes import primes_below
from ..shared.solver import Solver
import divisors as dl
from multiprocessing import Pool

limit = 100_000_000
primes = list(primes_below(limit))
prime_set = set(primes)

def is_prime(n: int) -> bool:
    if n > limit:
        raise Exception('Out of range')
    return n in prime_set

def divisors(n):
    return dl.divisors(n, primes)

def as_special(n: int):
    for d in divisors(n):
        x = d + n // d
        if not is_prime(x):
            return 0
    return n

def _solve(print=print):
    candidates = (p-1 for p in primes[1:])
    with Pool() as p:
        specials = p.map(as_special, candidates)
        total = sum(specials)
        print(total)
        return True
    return False



description = '''Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.
'''

solver = Solver(357,
                'Prime generating integers',
                description,
                _solve
                )