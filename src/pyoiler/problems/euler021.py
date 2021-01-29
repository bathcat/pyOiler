from ..shared.solver import Solver
from sympy import proper_divisors



def d(n:int):
    ds = proper_divisors(n,generator=True)
    return sum(ds)

def get_amicable_sibling(n:int):
    d_n=d(n)
    if d(d_n)==n:
        return d_n
    return None

def _solve(print=print):
    max_exclusive=10_001
    amicables = set()
    non_amicables=set()

    for i in range(max_exclusive):
        if i in amicables or i in non_amicables:
            continue
        sib = get_amicable_sibling(i)
        if sib:
            amicables.add(i)
            amicables.add(sib)
        else:
            non_amicables.add(sib)
    
    print(f'Result: {sum(amicables)}')

    return True

description = '''
Let d(n) be defined as the sum of proper divisors of n (numbers less 
than n which divide evenly into n). 

If 
    d(a) = b 
      and 
    d(b) = a, 
      where 
    a ≠ b, 

then a and b are an amicable pair and each of a and b are called 
amicable numbers.

For example, the proper divisors of 220 are 
    1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. 

The proper divisors of 284 are 
    1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

solver = Solver(21,
                'Amicable numbers',
                description,
                _solve
                )