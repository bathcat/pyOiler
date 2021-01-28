from typing import List


def multiply(xs: List[int]):
    result = 1
    for x in xs:
        result = result * x
    return result

def add(xs: List[int]):
    total = 0
    for x in xs:
        total += x
    return total
