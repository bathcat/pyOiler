import itertools as it
from typing import Iterable, List, Callable, TypeVar, Generic
import toolz


def nth(iterable: Iterable, n: int, default=None):
    "Returns the nth item or a default value"
    return next(it.islice(iterable, n, None), default)


def take(n: int, seq: Iterable) -> Iterable:
    return toolz.take(n, seq)

def has_count(n:int, seq: Iterable) -> bool:
    iterator = iter(seq)
    for i in range(n):
        if next(iterator, None) is None:
            return False
    return next(iterator, None) is None


T = TypeVar('T')
Predicate = Callable[[T], bool]


def take_while(p: Predicate, xs: Iterable[T]) -> Iterable[T]:
    return it.takewhile(p, xs)


def skip_while(p: Predicate, xs: Iterable[T]) -> Iterable[T]:
    return it.dropwhile(p,xs)

last = toolz.last
filter = toolz.filter
skip = toolz.drop
first = toolz.first
count = toolz.count
distinct = toolz.unique


def head(iterable):
    return list(it.islice(iterable, 1))[0]


def flat_map(f, items):
    return it.chain.from_iterable(map(f, items))


def all_equal(iterable: Iterable) -> bool:
    zero = head(iterable)
    for element in iterable:
        if element != zero:
            return False
    return True


def skip_while(predicate: Callable, xs: Iterable):
    # This implementation seems hokey.
    skip_count = 0
    for x in xs:
        if not predicate(x):
            break
        skip_count += 1
    yield from toolz.drop(skip_count, xs)


def overlapping_windows(size: int, xs: List):
    last_window = len(xs) - size + 1
    for pos in range(0, last_window):
        yield xs[pos:pos + size]


def all_but_last(xs: Iterable) -> Iterable:
    iterator = iter(xs)
    previous = next(iterator, None)
    current = next(iterator, None)
    while current:
        yield previous
        previous = current
        current = next(iterator, None)


def combinations(xs, window_size=2):
    def non_unique_combos(xs, window_size=2):
        cached = set(take(window_size, xs))
        for x in xs:
            cached.add(x)
            yield from [frozenset(c) for c in it.combinations(cached, window_size)]

    yield from [list(s) for s in toolz.unique(non_unique_combos(xs, window_size))]

# def eager(generator):
#     @wraps(generator)
#     def wrapper(*args, **kwds):
#         return list(generator(*args, **kwds))
#     return wrapper
