from ..shared.solver import Solver
from typing import Iterable
from sympy.ntheory.digits import digits as s_digits

def get_digits(n:int)->Iterable[int]:
    return s_digits(n)[1:]

def get_digit_power_sum(n:int,power:int)->int:
    digit_powers=[d**power for d in get_digits(n)]
    return sum(digit_powers)

def is_digit_power_sum(n:int,power:int)->bool:
    return n==get_digit_power_sum(n,power)

def _solve(print = print):
    power=5
    limit = 100_000
    dpss = [n for n in range(2,limit) if is_digit_power_sum(n,power)]
    print(f'Result: {sum(dpss)}')
    return False


description = '''
Surprisingly there are only three numbers that can be written as the 
sum of fourth powers of their digits:

    1634 = 1**4 + 6**4 + 3**4 + 4**4
    8208 = 8**4 + 2**4 + 0**4 + 8**4
    9474 = 9**4 + 4**4 + 7**4 + 4**4

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth 
powers of their digits.

'''

solver = Solver(30,
                'Digit fifth powers',
                description,
                _solve
                )
