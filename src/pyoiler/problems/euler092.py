from typing import Iterable
from ..shared.solver import Solver
from ..shared.digits import to_digits_stream
from ..shared.more_itertools import count

def square(n:int)->int:
    return n*n

def digit_square_sum(n: int) -> int:
    fs = map(square, to_digits_stream(n))
    return sum(fs)

def digit_square_chain(n:int)->Iterable[int]:
    yield n
    history = {n}
    current = digit_square_sum(n)
    while not(current in history):
        yield current
        history.add(current)
        current = digit_square_sum(current)
    yield current

def arrives_at_89(n:int)->bool:
    for term in digit_square_chain(n):
        if term == 89:
            return True
    return False

def _solve(print=print):
    max_exclusive = 1_000_000
    arrivals = filter(arrives_at_89, range(1,max_exclusive))
    print(f"How many starting numbers below {max_exclusive} will arrive at 89?")
    print(count(arrivals))
    return True

description = '''A number chain is created by continuously adding the square of the digits in a number to form a new
number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY
starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?


'''

solver = Solver(92,
                'Square digit chains',
                description,
                _solve
                )
