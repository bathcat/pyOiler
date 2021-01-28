from typing import Iterable
from ..shared.solver import Solver

from ..shared.primes import is_prime
from ..shared.more_itertools import take

def t(n: int) -> int:
    return 2 * n * n - 1

def ts() -> Iterable[int]:
    i = 2
    while True:
        yield t(i)
        i += 1

def prime_ts() -> Iterable[int]:
    for term in ts():
        if is_prime(term):
            yield term

def run():
    max_n=10000
    primes = 0
    for n in range(2, max_n):
        if is_prime(t(n)):
            primes+=1
    print("Found a few primes:")
    print(primes)


def _solve(print=print):
    raise NotImplementedError
    return False

description = '''Consider numbers t(n) of the form t(n) = 2n**2-1 with n > 1.
The first such numbers are 7, 17, 31, 49, 71, 97, 127 and 161.
It turns out that only 49 = 7*7 and 161 = 7*23 are not prime.
For n ≤ 10000 there are 2202 numbers t(n) that are prime.

How many numbers t(n) are prime for n ≤ 50,000,000 ?
'''

solver = Solver(216,
                'Investigating the primality of numbers of the form 2n**2-1',
                description,
                _solve
                )
