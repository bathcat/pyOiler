from typing import List
from itertools import count
from ..shared.solver import Solver


def divides_evenly(n: int, divisors: List[int]):
    return all(n % d == 0 for d in divisors)

def _solve(print=print):
    divisors = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    divisors.reverse()

    for n in count(20*19, 20*19):
        if divides_evenly(n, divisors):
            print("Here it is: " + str(n))
            break
    return True


description = '''2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

solver = Solver(5,
                'Smallest multiple',
                description,
                _solve
                )
