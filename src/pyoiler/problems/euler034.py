from typing import Iterable
import itertools as it
from ..shared.solver import Solver
from ..shared.digits import digit_factorial_sum


def is_curious(n:int)->bool:
    return n == digit_factorial_sum(n)

def curious_numbers(up_to:int = None) -> Iterable[int]:
    for i in it.count(3):
        if is_curious(i):
            yield i
        if up_to and (i>= up_to):
            return

def _solve(print = print):
    limit = 10**6
    print(f"Here's the total: {sum(curious_numbers(limit))}")
    print("(It seems like the only curious numbers are 145 and 40585.)")
    return True


description = '''145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

solver = Solver(34,
                'Digit factorials',
                description,
                _solve
                )
