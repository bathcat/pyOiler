from typing import Iterable
from ..shared.solver import Solver
from ..shared.divisors import proper_divisors
from enum import Enum
from itertools import count as ints
from ..shared.more_itertools import take

class PerfectionLevel(Enum):
    Perfect = 1
    Deficient = 2
    Abundant = 3

def level_of(n:int) -> PerfectionLevel:
    total = sum(proper_divisors(n))
    if total > n:
        return PerfectionLevel.Abundant
    if total < n:
        return PerfectionLevel.Deficient
    return PerfectionLevel.Perfect

def abundants() -> Iterable[int]:
    return (i for i in ints(2,2) if level_of(i) == PerfectionLevel.Abundant)

def _solve(print = print):
    print('Not done.')
    return False


description = '''A perfect number is a number for which the sum of its 
proper divisors is exactly equal to the number. For example, the sum of 
the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means 
that 28 is a perfect number. 

A number n is called deficient if the sum of its proper divisors is less 
than n and it is called abundant if this sum exceeds n. 

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the 
smallest number that can be written as the sum of two abundant numbers 
is 24. By mathematical analysis, it can be shown that all integers greater 
than 28123 can be written as the sum of two abundant numbers. However, 
this upper limit cannot be reduced any further by analysis even though it 
is known that the greatest number that cannot be expressed as the sum of 
two abundant numbers is less than this limit. 

Find the sum of all the positive integers which cannot be written as the 
sum of two abundant numbers.

'''

solver = Solver(23,
                'Non-abundant sums',
                description,
                _solve
                )
