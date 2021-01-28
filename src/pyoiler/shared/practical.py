from itertools import combinations
from divisors import divisors

def is_practical(p_candidate: int) -> bool:
    if p_candidate < 1:
        return False

    if p_candidate==1:
        return True

    divisors = list(divisors(p_candidate))
    sums = set(divisors)
    arity = 1

    def get_sums(arity:int):
        return [sum(c) for c in combinations(divisors, arity)]

    def is_divisor_sum(ds_candidate):
        nonlocal arity
        nonlocal sums
        if ds_candidate in sums:
            return True
        while arity <= len(divisors):
            arity+=1
            more_sums = get_sums(arity)
            sums = sums.union(more_sums)
            if ds_candidate in sums:
                return True
        return False

    for i in range(1, p_candidate):
        if not is_divisor_sum(i):
            return False

    return True


def test_is_practical():
    known_practicals = [
        1, 2, 4, 6, 8, 12, 16, 18, 20, 24, 28, 30, 32, 36, 40, 42, 48, 54, 56,
        60, 64, 66, 72, 78, 80, 84, 88, 90, 96, 100, 104, 108, 112, 120,
        126, 128, 132, 140, 144, 150
    ]
    for p in known_practicals:
        if not is_practical(p):
            raise Exception(f'Should be Practical: {p}')

    for np in [i for i in range(1,max(known_practicals)+1) if i not in known_practicals]:
        if is_practical(np):
            raise Exception(f'Should not be Practical: {np}')