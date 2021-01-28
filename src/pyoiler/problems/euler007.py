import rx
from rx import operators as ops
from ..shared.primes import primes
from ..shared.solver import Solver



def _solve(print=print):
    v = rx.from_iterable(primes()) \
      .pipe(
        ops.skip(10000),
        ops.take(1),
    ).run()
    print(v)
    return True


description = '''By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

solver = Solver(7,
                '10001st prime',
                description,
                _solve
                )
