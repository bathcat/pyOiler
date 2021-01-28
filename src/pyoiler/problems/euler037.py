from ..shared.digits import to_digits, from_digits
from ..shared.solver import Solver
from ..shared.primes import PrimeCache
from ..shared.more_itertools import take, skip_while
from ..shared.list_arithmatic import add


def truncations_left(n: int):
    ds = to_digits(n)
    count = len(ds)
    if count == 1:
        yield n
    for i in range(1, len(ds)):
        yield from_digits(ds[:count-i])

def truncations_right(n: int):
    ds = to_digits(n)
    count = len(ds)
    if count == 1:
        yield n
    for i in range(1, len(ds)):
        yield from_digits(ds[i:])

cached = PrimeCache(1000000)

def is_truncatable(n:int):
    for ln in truncations_left(n):
        if not cached.is_prime(ln):
            return False
    for rn in truncations_right(n):
        if not cached.is_prime(rn):
            return False
    return True

def _solve(print=print):
    truncatable_primes = (p for p in skip_while(lambda x: x<10, cached.primes()) if is_truncatable(p))
    first_11 = list(take(11, truncatable_primes))

    print(f'Here are the first 11 truncatable primes:{first_11}')
    print(f"Here's the sum:{add(first_11)}")

    return True

description = '''The number 3797 has an interesting property. Being prime itself, it is possible to continuously 
remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from 
right to left: 3797, 379, 37, and 3. 

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

solver = Solver(37,
                'Truncatable primes',
                description,
                _solve
                )