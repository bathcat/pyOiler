from ..shared.solver import Solver

def square_of_sum(n:int)->int:
    added_up = sum(range(n+1))
    return added_up ** 2

def sum_of_squares(n:int)->int:
    return sum([x*x for x in range(n+1)])

def sum_square_difference(n:int)->int:
    return square_of_sum(n) - sum_of_squares(n)


def _solve(print=print):
    print(sum_square_difference(100))
    return True


description = '''The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''

solver = Solver(6,
                'Sum square difference',
                description,
                _solve
                )
