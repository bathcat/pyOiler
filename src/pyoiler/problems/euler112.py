from typing import Iterable
from ..shared.digits import to_big_end_digits
from ..shared.solver import Solver


def is_increasing(xs: Iterable[int]):
    previous = 0
    for x in xs:
        if x < previous:
            return False
        previous = x
    return True

def is_decreasing(xs: Iterable[int]):
    previous = 9
    for x in xs:
        if x > previous:
            return False
        previous = x
    return True

def is_increasing_integer(x:int):
    return is_increasing(to_big_end_digits(x))

def is_decreasing_integer(x:int):
    return is_decreasing(to_big_end_digits(x))

def is_bouncy_integer(x:int)->bool:
    digits = to_big_end_digits(x)
    return (not is_increasing(digits)) and (not is_decreasing(digits))


def _solve(print=print):
    raise Exception('Not Done!')
    count = 540
    bounces=0
    for n in range(0,count):
        if is_bouncy_integer(n):
            bounces+=1
    print('Bounce fraction: ')
    print(bounces/count)
    print()
    return False

description = '''Working from left-to-right if no digit is exceeded by the digit to its left it is called an 
increasing number; for example, 134468. 

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (
525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538. 

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy 
numbers is equal to 90%. 

Find the least number for which the proportion of bouncy numbers is exactly 99%.
'''

solver = Solver(112,
                'Bouncy numbers',
                description,
                _solve
                )