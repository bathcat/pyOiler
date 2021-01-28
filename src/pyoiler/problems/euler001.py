import rx
from rx import operators as ops
from ..shared.solver import Solver, t_print

def _solve(print: t_print = print) -> bool:
    limit = 1000
    total = rx.range(limit) \
        .pipe(
        ops.filter(lambda n: n % 3 == 0 or n % 5 == 0),
        ops.sum(),
    ).run()
    print(total)
    return True

description = '''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
                
Find the sum of all the multiples of 3 or 5 below 1000.
'''


solver = Solver(1,
                'Multiples of 3 and 5',
                description,
                _solve
                )