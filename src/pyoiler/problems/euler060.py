from typing import List
from ..shared.primes import is_prime, primes
from itertools import permutations, combinations
from ..shared.digits import concatenate_digits
from toolz import take, memoize
from ..shared.solver import Solver

import multiprocessing as mp


uri = 'https://projecteuler.net/problem=60'
problem_number = 60
name = "Prime pair sets"
description = """The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in 
any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these 
four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

"""

@memoize
def is_prime_tuple(a: int, b: int) -> bool:
    c = concatenate_digits(a, b)
    return is_prime(c)


def is_remarkable(ps: List[int]) -> bool:
    for a, b in permutations(ps, 2):
        if not is_prime_tuple(a, b):
            return False
    return True


def is_remarkable_2(ps: List[int]):
    return is_remarkable(ps), ps


def _solve(print=print):
    print('This isn''t really done. Groups of 4 works ok, but 5s take forever.')
    print('Coming up with a lazy version of combinations would be better')

    with mp.Pool(4) as pool:
        cs = combinations(take(200, primes()), 4)

        for remarkable, combo in pool.imap_unordered(is_remarkable_2, cs, chunksize=125):
            if remarkable:
                print(combo)

    return False

description = '''The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''

solver = Solver(60,
                'Prime pair sets',
                description,
                _solve
                )