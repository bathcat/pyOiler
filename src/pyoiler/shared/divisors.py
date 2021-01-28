from functools import reduce
from typing import Iterable
from .more_itertools import all_but_last
import operator as op

def get_factors(n:int, primes:Iterable[int]):
    for p in primes:
        if p * p > n//2:
            break
        count = 0
        while not n % p:
            n //= p
            count += 1
        if count > 0:
            yield p, count
    if n > 1:
        yield n, 1

def divisors(n,primes:Iterable[int]):
    if n==1:
        yield 1
        return

    fs = list(get_factors(n,primes))
    nfactors = len(fs)
    f = [0] * nfactors
    while True:
        xs = (fs[x][0]**f[x] for x in range(nfactors))
        yield reduce(op.mul,xs, 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= fs[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return


def proper_divisors(n:int,primes:Iterable[int])->Iterable[int]:
    return all_but_last(divisors(n,primes))

