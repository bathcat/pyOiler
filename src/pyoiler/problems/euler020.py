from ..shared.solver import Solver
import math as m
from ..shared.digits import to_digits



def _solve(print = print):
    n = 100
    f_n = m.factorial(n)
    ds = sum(to_digits(f_n))
    print(f"n: {n}")
    print(f"f(n): {f_n}")
    print(f"Digit sum: {ds}")

    return True


description = '''n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

solver = Solver(20,
                'Factorial digit sum',
                description,
                _solve
                )
