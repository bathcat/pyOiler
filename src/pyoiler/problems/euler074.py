from typing import Iterable
from ..shared.solver import Solver
from ..shared.digits import digit_factorial_sum
from ..shared.more_itertools import count, has_count
from multiprocessing import Pool

def digit_factorial_chain(n:int)->Iterable[int]:
    yield n
    history = {n}
    current = digit_factorial_sum(n)
    while not(current in history):
        yield current
        history.add(current)
        current = digit_factorial_sum(current)
    yield current

def chain_term_count(n:int)->int:
    return count(digit_factorial_chain(n))-1

def _solve(print=print):
    with Pool() as p:
        max_exclusive = 1000000
        chain_length = 60

        chain_lengths = p.map(chain_term_count, range(2,max_exclusive), 75)

        print(f"Chains starting < {max_exclusive} containing exactly {chain_length} non-repeating terms:")
        chains_of_length = (i for i in chain_lengths if i == chain_length)
        print(count(chains_of_length))

        return True


description = '''The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

'''

solver = Solver(74,
                'Digit factorial chains',
                description,
                _solve
                )
