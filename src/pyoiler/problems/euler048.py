from itertools import count
from typing import Iterable
from ..shared.more_itertools import take

from ..shared.solver import Solver

def self_powers() -> Iterable[int]:
    return (i**i for i in count(1))

def self_power_sum(up_to:int)->int:
    return sum(take(up_to,self_powers()))

def _solve(print = print):
    up_to = 1000
    d_count = 10
    t = self_power_sum(up_to)
    t_as_str = str(t)

    print(f"Sum of self power series <= {up_to} is a {len(t_as_str)} digit number, starting with {t_as_str[:d_count]}.")

    last_digits = t_as_str[-1*d_count:]
    print(f"The last {d_count} digits are: {last_digits}")
    return True

description = '''The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

solver = Solver(48,
                "Self powers",
                description,
                _solve
                )
