from ..shared.solver import Solver
import gmpy2



 
def tetration_mod(a:int,height:int,digits:int)->int:
    """Gets the rightmost digits of a tetration operation

       Notes:
       1. Wikipedia's entry on [Graham's number](https://en.wikipedia.org/wiki/Graham%27s_number)
          describes an algorithm for getting the rightmost digits of a tetration operation:

          > A simple algorithm for computing these digits may be described as follows: 
          > let x = 3, then iterate, d times, the assignment x = 3**x mod 10d. Except for omitting 
          > any leading 0s, the final value assigned to x (as a base-ten numeral) is then composed 
          > of the d rightmost decimal digits of 3↑↑n, for all n > d. (If the final value of x 
          > has fewer than d digits, then the required number of leading 0s must be added.)  

       2. Native python is painfully slow; using [GMP](http://gmplib.org) for 
          integer operations is way faster. 

          See also https://gmpy2.readthedocs.io/en/latest/index.html

    Args:
        a (int): Argument
        height (int): Height
        digits (int): Number of rightmost digits to capture

    Returns:
        int: Rightmost digits
    """
    result = gmpy2.xmpz(a)
    for i in range(1,min(height,digits+1)):
        result = (a**result)%(10**digits) 
    return result        



def _solve(print = print):
    a=1777
    height=1855
    digits = 8
    print(f'Answer: {tetration_mod(a,height,digits)}')

    return True

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
