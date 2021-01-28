from itertools import count
from typing import Iterable

from ..shared.solver import Solver
from ..shared.primes import primes_below

max_p = 100_000
primes = primes_below(max_p)
set_primes = frozenset(primes)

def is_prime(n: int) -> bool:
    if n > max_p:
        raise Exception('Out of range')
    return abs(n) in set_primes

def consecutive_primes(a:int,b:int, max_n:int = None)->Iterable[int]:
    ns = range(0,max_n) if max_n else count()
    for n in ns:
        result = n**2 + a*n + b
        if not is_prime(result):
            return
        yield result

def formula_results(max_a:int, max_b:int):
    candidate_bs = range(max_b*-1, max_b)
    #cheat a bit here 'cause 0+0+b has to be prime.
    candidate_bs = [b for b in candidate_bs if is_prime(b)]

    #maybe cheat more here, 'cause a+b+1 have to be prime. Which is odd (or 2)... dunno.
    candidate_as = range(max_a*-1, max_a)

    for b in candidate_bs:
        for a in candidate_as:
            if not is_prime(a+b+1):
                continue
            yield a,b, list(consecutive_primes(a,b))

def _solve(print=print):
    max_a = 1000
    max_b = 999
    results = formula_results(max_a,max_b)
    a,b,ps = max(results,key=lambda t:len(t[2]))

    print("Here's that prime series generating formula:")
    print(f"a:{a} b:{b} len(ps): {len(ps)} ps: {ps}")

    return True

description = '''Euler discovered the remarkable quadratic formula:

n^2+n+41

It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
. However, when n=40,40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,41^2+41+41

is clearly divisible by 41.

The incredible formula n^2−79n+1601
was discovered, which produces 80 primes for the consecutive values 0≤n≤79

. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

    n^2+an+b

, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of 
primes for consecutive values of n, starting with n=0. 

'''

solver = Solver(27,
                'Quadratic primes',
                description,
                _solve
                )