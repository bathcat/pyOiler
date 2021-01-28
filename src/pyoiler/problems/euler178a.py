from ..shared.digits import is_pandigital
import multiprocessing
import random
import time
from threading import current_thread

import rx
from rx.scheduler import ThreadPoolScheduler
from rx import operators as ops


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
    limit = 10 ** 22
    optimal_thread_count = multiprocessing.cpu_count()
    pool_scheduler = ThreadPoolScheduler(optimal_thread_count)

    count = rx.from_iterable(pandigital_step_numbers()) \
        .pipe(
        ops.take_while(lambda n: n < limit),
        ops.count(),
    ) \
        .run()

    onComplete(count)

    # print('How many pandigital step numbers less than 10**40 are there? ')
    # count = 0
    # for n in pandigital_step_numbers():
    #     if n >= 10 ** 25:
    #         break
    #     count += 1
    #     if count % 15000 == 0:
    #         print('[sample: ' + str(n) + ']')
    # print('--------------------------')
    # print('Total:')
    # print(count)
