from ..shared.solver import Solver


def _solve(print = print):
    return False

description = '''The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

'''

solver = Solver(47,
                "Distinct primes factors",
                description,
                _solve
                )
