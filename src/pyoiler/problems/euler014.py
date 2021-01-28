from typing import Dict
from ..shared.cache import memoize
from ..shared.solver import Solver

def to_next(i: int):
    if i % 2 == 0:
        return i // 2
    return 3 * i + 1

def sequence(start: int = 1):
    yield start
    while start != 1:
        start = to_next(start)
        yield start


@memoize
def rsequence(n: int = 1):
    yield n
    if n == 1:
        return
    nplusone = to_next(n)
    for x in rsequence(nplusone):
        yield x

class SequenceCalculator():
    cache: Dict[int, int] = {
        1: None,
    }

    def from_cache(self, start:int):
        current = start
        while current is not None:
            yield current
            current = self.cache[current]

    def sequence(self, start: int = 1):
        if start in self.cache:
            for n in self.from_cache(start):
                yield n
            return

        next = to_next(start)
        self.cache[start] = next
        yield start

        for n in self.sequence(next):
            yield n


def _solve(print=print):
    calc = SequenceCalculator()

    longest = []
    for i in range(1, 1000000):
        current = list(sequence(i))
        if len(current) > len(longest):
            longest = current

    print(f"Here's the longest:{longest}")

    return True

description = '''The following iterative sequence is defined for the set of positive integers:
   n → n/2 (n is even)
   n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
   13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.'''

solver = Solver(14,
                'Longest Collatz sequence',
                description,
                _solve
                )