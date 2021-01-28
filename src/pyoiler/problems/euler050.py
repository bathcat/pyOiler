from typing import Iterable
from ..shared.solver import Solver
import primes as p
from ..shared.more_itertools import take_while

def down_range(_min:int,_max:int)-> Iterable[int]:
    return reversed(range(_min, _max))

def longest_prime_sum_window(upper_limit:int):
    primes = list(take_while(lambda p: p < upper_limit, p.primes()))
    primes_set = frozenset(primes)
    previous_window_total = sum(primes)

    def is_prime(n: int) -> bool:
        return n in primes_set

    for w_size in down_range(2, len(primes)):
        last_window = len(primes) - w_size + 1
        previous_window_total =total = previous_window_total - primes[w_size]
        if is_prime(total):
            return primes[: w_size], total
        if w_size%2==0:
            continue
        pos = 1
        while (pos < last_window) and (total <= upper_limit):
            previous = primes[pos-1]
            current = primes[pos + w_size - 1]
            total = total - previous + current
            if is_prime(total):
                return primes[pos:pos + w_size], total
            pos+=1


def _solve(print = print):
    limit = 1_000_000
    terms,target = longest_prime_sum_window(limit)
    print(f"The longest sum of consecutive primes below {limit} that adds to a prime, contains {len(terms)} terms, "
          f"and is equal to {target}.")
    return True

description = '''The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

'''

solver = Solver(50,
                "Consecutive prime sum",
                description,
                _solve
                )
