from ..shared.fibonacci import  fibonacci_term
from ..shared.digits import digit_count
from ..shared.solver import Solver



def _solve(print=print):
    for index in range(0, 10000):
        term = fibonacci_term(index)
        digits = digit_count(term)
        if digits >= 1000:
            print('Index: '+str(index))
            print('Digit count: ' + str(digits))
            print('Value: ' + str(term))
            return True
    return False

description = '''The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.

Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''

solver = Solver(25,
                '1000-digit Fibonacci number',
                description,
                _solve
                )