from typing import Iterable
import math
from ..shared.solver import Solver
from itertools import count
from ..shared.more_itertools import take

def power_digits(n:int) -> Iterable[int]:
    max_exclusive = 10 ** n
    _min = 10 ** (n-1)
    start= math.floor(10 ** (1/n))
    powers = ((i,i**n) for i in count(start))
    i,p = next(powers)
    while p < max_exclusive:
        if p >= _min:
            yield n,i,p
        i,p = next(powers)

def all_power_digits(limit:int)->Iterable[int]:
    for i in range(2,limit):
        yield from power_digits(i)

def _solve(print = print):
    limit = 10_000
    pds = list(all_power_digits(limit))
    print(f"For some reason, probably deep and mathy, there are only {len(pds)} n-digit integers which are also an nth power")
    print(f"And here they are:")
    for p,n,r in pds:
        print(f"     {n}^{p} = {r}")
    return True

description = '''The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, 
is a ninth power. 

How many n-digit positive integers exist which are also an nth power?

'''

solver = Solver(63,
                "Powerful digit counts",
                description,
                _solve
                )
