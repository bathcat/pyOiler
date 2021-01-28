from cache import memoize
from more_itertools import nth


@memoize
def fibonacci():
    t_minus_2 = 0
    t_minus_1 = 1
    yield 1
    while True:
        current = t_minus_1 + t_minus_2
        yield current
        t_minus_2 = t_minus_1
        t_minus_1 = current


def fibonacci_term(n: int = 0):
    return nth(fibonacci(), n)
