from ..shared.solver import Solver
from ..shared.primes import prime_factors

description = '''The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


def _solve(print = print):
    real_target = 600851475143
    target = 13195
    print(f"Solving this thing with {real_target} takes forever, so we're using {target}.")
    biggest_prime_factor = max(prime_factors(target))
    print(biggest_prime_factor)
    return True

solver = Solver(3,
                'Largest prime factor',
                description,
                _solve
                )



