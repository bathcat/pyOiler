from typing import Iterable, Tuple

from practical import is_practical
from ..shared.solver import Solver
import primes
from toolz import sliding_window
from ..shared.more_itertools import first


def is_super_practical(n):
    # check_on = [n-8, n-4, n, n+4, n+8]
    check_on = [n-4,n,]
    return all(is_practical(n) for n in check_on)

def consectuive_pairs(xs: Iterable) -> Iterable[Tuple]:
    n_minus_1 = first(xs)
    for n in xs:
        yield n_minus_1, n
        n_minus_1 = n


def sexy_prime_pairs():
    for pair in consectuive_pairs(primes.primes()):
        if pair[0] + 6 == pair[1]:
            yield pair

def sexy_triples():
    for ps in sliding_window(4, primes.primes()):
        if ps[0] + 6  == ps[1] and \
           ps[1] + 6 == ps[2] and \
           ps[2] + 6 == ps[3]:
            yield ps[1] + 3

def sexy_super_practicals():
    return (t for t in sexy_triples() if is_super_practical(t))



def _solve(print=print):
    print('TODO: Come up with a better way of testing practicality.')
    print('Good wiki articles:')
    print('https://en.wikipedia.org/wiki/Practical_number')
    print('https://en.wikipedia.org/wiki/Divisor_function')

    return False


description = '''Consider the number 6. The divisors of 6 are: 1,2,3 and 6.

Every number from 1 up to and including 6 can be written as a sum of distinct divisors of 6:
1=1, 2=2, 3=1+2, 4=1+3, 5=2+3, 6=6.

A number n is called a practical number if every number from 1 up to and including n can be expressed as a sum of 
distinct divisors of n. 

A pair of consecutive prime numbers with a difference of six is called a sexy pair (since "sex" is the Latin word for 
"six"). The first sexy pair is (23, 29). 

We may occasionally find a triple-pair, which means three consecutive sexy prime pairs, such that the second member 
of each pair is the first member of the next pair. 

We shall call a number n such that :

    (n-9, n-3), (n-3,n+3), (n+3, n+9) form a triple-pair, and
    the numbers n-8, n-4, n, n+4 and n+8 are all practical, 

an engineers’ paradise.

Find the sum of the first four engineers’ paradises.


'''

solver = Solver(263,
                'An engineers''s dream come true',
                description,
                _solve
                )
