from ..shared.digits import is_pandigital
from ..shared.solver import Solver


def is_step_number(n: int) -> bool:
    if n < 10:
        return False
    ones_place = n % 10
    truncated = n // 10
    tens_place = truncated % 10
    if abs(ones_place - tens_place) != 1:
        return False
    if truncated < 10:
        return True
    return is_step_number(truncated)


def step_children(n: int):
    if n == 0:
        return
    ones_place = n % 10
    if ones_place == 0:
        yield 10 * n + 1
        return
    if ones_place == 9:
        yield 10 * n + 8
        return
    yield 10 * n + ones_place + 1
    yield 10 * n + ones_place - 1


def step_numbers():
    last_gen = list(range(1, 10))
    while True:
        next_gen = []
        for g0 in last_gen:
            for g1 in step_children(g0):
                yield g1
                next_gen.append(g1)
        last_gen = next_gen


def pandigital_step_numbers():
    for n in step_numbers():
        if is_pandigital(n):
            yield n


def run(onComplete=lambda: None):
    print('How many pandigital step numbers less than 10**40 are there? ')
    count = 0
    limit = 10 ** 29
    for n in pandigital_step_numbers():
        if n >= limit:
            break
        count += 1
        if count % 85000 == 0:
            print('[sample: ' + str(n) + ']')
    onComplete(count)

def _solve(print=print):
    raise NotImplementedError
    return False

description = '''Consider the number 45656.
It can be seen that each pair of consecutive digits of 45656 has a difference of one.
A number for which every pair of consecutive digits has a difference of one is called a step number.
A pandigital number contains every decimal digit from 0 to 9 at least once.
How many pandigital step numbers less than 1040 are there? '''

solver = Solver(178,
                'Step Numbers',
                description,
                _solve
                )
