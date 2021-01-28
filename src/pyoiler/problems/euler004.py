from itertools import product
from ..shared.solver import Solver
from ..shared.digits import is_palindrome




def _solve(print=print):
    xs = list(range(100, 1000))
    palindromes =  [(x, y, x*y) for x,y in product(xs, xs) if is_palindrome(x*y)]
    biggest = max(palindromes, key=lambda t: t[2])
    print(biggest)
    return True

description = '''A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

solver = Solver(4,
                'Largest palindrome product',
                description,
                _solve
                )
