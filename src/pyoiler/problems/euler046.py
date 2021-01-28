from typing import Iterable
from ..shared.solver import Solver
from ..shared.primes import composites, primes
from itertools import count, combinations
from ..shared.more_itertools import take_while, skip_while, take

def double_squares()->Iterable[int]:
    return (2*i*i for i in count(1))

def odd_composites() -> Iterable[int]:
    return (c for c in composites() if c%2==1)

def is_goldbachian(n:int)->bool:
    ps = list(take_while(lambda p1: p1<n,primes()))
    for ds in take_while(lambda d: d<n,double_squares()):
        for p in ps:
            if (ds + p) == n:
                return True
    return False


def _solve(print = print):
    for oc in odd_composites():
        if not is_goldbachian(oc):
            print(f"{oc} is not goldbachian!")
            return True
    return False

description = '''It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a 
prime and twice a square. 

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

solver = Solver(46,
                "Goldbach's other conjecture",
                description,
                _solve
                )
