from typing import Iterable
import math
from ..shared.solver import Solver
from fractions import Fraction
from ..shared.more_itertools import first


# Useful links:
# https://proofwiki.org/wiki/Continued_Fraction_Expansion_of_Irrational_Square_Root/Example/13/Convergents
# https://en.wikipedia.org/wiki/Pell%27s_equation





def is_square(n:int)->bool:
    return math.sqrt(n).is_integer()

def is_solution(x,y,d):
    return x**2 - d*(y**2) == 1

def continued_fraction_expansion(s: int) -> Iterable[int]:
    p = 0
    q = 1
    guess =math.floor(math.sqrt(s))
    a = guess
    while True:
        yield a
        p = a * q - p
        q = (s - p ** 2) / q
        a = math.floor((guess + p)/q)

def convergents(s:int) -> Iterable[Fraction]:
    expansion = continued_fraction_expansion(s)
    a_0 = first(expansion)
    a_1 = first(expansion)
    p_m_2 = a_0
    q_m_2 = 1
    yield  Fraction(p_m_2,q_m_2)

    p_m_1 = a_0*a_1 + 1
    q_m_1 = a_1
    yield Fraction(p_m_1,q_m_1)

    for a in expansion:
        p = a*p_m_1 + p_m_2
        q = a * q_m_1 + q_m_2
        yield Fraction(p, q)
        p_m_2 = p_m_1
        p_m_1 = p

        q_m_2 = q_m_1
        q_m_1 = q


def minimal_x_solution(d: int):
    for r in convergents(d):
        x = r.numerator
        y = r.denominator
        if is_solution(x,y,d):
            return r


def _solve(print=print):
    all_the_d = 1000
    non_squares = (d for d in range(all_the_d) if not is_square(d))
    solutions = [(d,minimal_x_solution(d)) for d in non_squares]
    biggest_x = max(solutions,key=lambda s: s[1].numerator)
    print(f"Biggest x solution: {biggest_x} ")
    return True




description = '''Consider quadratic Diophantine equations of the form:

x**2 – Dy**2 = 1

For example, when D=13, the minimal solution in x is 649**2 – 13×180**2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3**2 – 2×2**2 = 1
2**2 – 3×1**2 = 1
9**2 – 5×4**2 = 1
5**2 – 6×2**2 = 1
8**2 – 7×3**2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

'''

solver = Solver(66,
                'Diophantine equation',
                description,
                _solve
                )
