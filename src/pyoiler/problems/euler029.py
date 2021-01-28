from typing import Iterable
from ..shared.more_itertools import distinct,count

from ..shared.solver import Solver

def distinct_combo_count(a:range, b:range) -> Iterable[int]:
    def get_cs():
        for a1 in a:
            for b1 in b:
                yield a1**b1
    return count(distinct(get_cs()))


def _solve(print = print):
    _min = 2
    _max = 100
    _as = range(_min,_max+1)
    _bs = range(_min,_max+1)
    c_count = distinct_combo_count(_as, _bs)
    print(f"How many distinct terms? {c_count}")

    return False


description = '''Consider all integer combinations of a^b for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:

    2^2=4, 2^3=8, 2^4=16, 2^5=32
    3^2=9, 3^3=27, 3^4=81, 3^5=243
    4^2=16, 4^3=64, 4^4=256, 4^5=1024
    5^2=25, 5^3=125, 5^4=625, 5^5=3125

If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:

4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125

How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?


'''

solver = Solver(29,
                'Distinct powers',
                description,
                _solve
                )
