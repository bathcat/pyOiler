from ..shared.primes import primes
import rx
from rx import operators as ops
from ..shared.solver import Solver

def _solve(print=print):
    total = rx.from_iterable(primes()) \
        .pipe(
        ops.take_while(lambda p: p < 2000000),
        ops.sum(),
    ).run()
    print(f'The sum of primes below 2m: {total}')
    return True

description = '''The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

solver = Solver(10,
                'Summation of primes',
                description,
                _solve
                )
