from ..shared.digits import to_digits
from ..shared.list_arithmatic import add
from ..shared.solver import Solver

def digit_sum(n:int):
    return add(to_digits(n))


def test_with_example():
    """2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26."""
    value = 2**15
    if value != 32768:
        raise Exception('Test failed')
    print('Value is: ' + str(value))
    added_up = digit_sum(value)
    if added_up != 26:
        raise Exception('Test failed')
    print('Digit sum is: ' + str(added_up))


def _solve(print=print):
    value = 2**1000
    print('Value is: ' + str(value))
    added_up = digit_sum(value)
    print('Digit sum is: ' + str(added_up))
    return True

description = '''2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

solver = Solver(16,
                'Power digit sum',
                description,
                _solve
                )