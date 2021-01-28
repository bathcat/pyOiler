import functools
import itertools

def memoize(f):
    cache = {}

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        k = args, frozenset(kwargs.items())
        it = cache[k] if k in cache else f(*args, **kwargs)
        cache[k], result = itertools.tee(it)
        return result

    return wrapper
