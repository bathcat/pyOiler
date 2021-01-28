from itertools import islice, count
from typing import List, FrozenSet, Iterable
from more_itertools import take_while
import random
import numpy as np


def primes() -> Iterable[int]:
    # Based on # http://code.activestate.com/recipes/117119/
    non_primes = {}
    yield 2
    odds = islice(count(3), 0, None, 2)
    for q in odds:
        p = non_primes.pop(q, None)
        if p is None:
            non_primes[q * q] = 2 * q
            yield q
        else:
            x = p + q
            while x in non_primes:
                x += p
            non_primes[x] = p

def primes_below_numpy(n):
    # Create B, setting all elements to True.
    B = np.ones(n + 1, dtype=np.bool)
    B[0:2] = False
    for i in range(2, n + 1):
        if B[i]:
            B[i*i: n+1: i] = False
    return np.arange(n + 1)[B]

def primes_below(n):
    return [int(p) for p in primes_below_numpy(n)]


def composites() -> Iterable[int]:
    ps = primes()
    previous = next(ps)
    for current in ps:
        yield from range(previous+1, current)
        previous = current


def is_prime(n:int, k:int=40)->bool:
    # Implementation uses the Miller-Rabin Primality Test
    # The optimal number of rounds for this test is 40
    # See http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    # for justification

    # If number is even, it's a composite number

    if n == 2 or n==3:
        return True

    if n % 2 == 0:
        return False

    r=0
    s=n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


class PrimeCache():
    max_cached: int = 2
    ps: List[int]
    ps_set: FrozenSet[int]

    def __init__(self, up_to: int):
        self.ps = list(primes_below(up_to))
        self.ps_set=frozenset(self.ps)
        self.max_cached = up_to

    def primes(self):
        return self.ps

    def is_prime(self,n):
        if n > self.max_cached:
            raise Exception('TODO: Expand cache dynamically.')
        return n in self.ps_set





def prime_factors(n: int):
    return (p for p in take_while(lambda p: p <= n / 2, primes()) if n % p == 0)

# _primes = frozenset(take(100000, primes()))
# _m = max(_primes)


# def is_prime(candidate: int) -> bool:
#     if candidate > _m:
#         raise Exception('Can''t count that high.')
#         # for p in takewhile(lambda i: candidate >= i, primes()):
#         #     _primes.add(p)
#     return candidate in _primes
