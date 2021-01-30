from ..shared.solver import Solver
import gmpy2
from gmpy2 import mpz, powmod, xmpz

"""[summary]

Note:
    https://en.wikipedia.org/wiki/Tetration
 
Maybe: 
    https://gmpy2.readthedocs.io/en/latest
    https://github.com/aleaxit/gmpy


"""

def hyperpow(a:int,b:int)->int:
    result = xmpz(a)
    for i in range(1,b):
        result = a**result 
    return result

# def hyperpow(a:int,b:int)->int:
#     result = a
#     for i in range(1,b):
#         result = a**result 
#     return result

def _solve(print = print):
    print(f'\n\n***************')
    gmpy2.get_context().precision=1024 ** 6
    

    ##print(gmpy2.get_context())

    print(f"3↑↑4 = {hyperpow(3,4)}")
    return False

description = '''
The hyperexponentiation or tetration of a number a by a positive integer 
b is recursively defined by:

  a↑↑1 = a,
  a↑↑(k+1) = a(a↑↑k).

Thus we have e.g. 3↑↑2 = 3^3 = 27, hence 3↑↑3 = 3^27 = 7625597484987 
and 3↑↑4 is roughly 103.6383346400240996*10^12.

Find the last 8 digits of 1777↑↑1855.

'''

solver = Solver(188,
                "The hyperexponentiation of a number",
                description,
                _solve
                )
