from typing import Iterable, List
import re
from math import factorial


rx = re.compile('(?=.*0)(?=.*1)(?=.*2)(?=.*3)(?=.*4)(?=.*5)(?=.*6)(?=.*7)(?=.*8)(?=.*9)')


def to_digits_stream(n: int = 0) -> Iterable[int]:
    while n > 0:
        yield n % 10
        n = n // 10


def to_digits(n: int):
    return list(to_digits_stream(n))


def to_big_end_digits(n: int = 0) -> Iterable[int]:
    digits = list(to_digits(n))
    digits.reverse()
    return digits


def is_palindrome(n: int):
    digits = to_digits(n)
    for i in range(0, len(digits)):
        if digits[i] != digits[(i + 1) * -1]:
            return False
    return True


def digit_count(n: int = 0) -> int:
    # TODO: Not very efficient. Maybe strings would be better?
    digits = list(to_digits(n))
    return len(digits)


def from_digits(xs: Iterable[int]) -> int:
    result = 0
    place = 0
    for d in xs:
        result = result + d * 10 ** place
        place += 1
    return result


def is_pandigital(n: int) -> bool:
    match = rx.match(str(n))
    return match is not None


def reverse_digits(n: int) -> int:
    digits = to_digits(n)
    digits.reverse()
    return from_digits(digits)


def concatenate_digits(l: int, r: int) -> int:
    return int(str(l) + str(r))


def digit_factorial_sum(n: int) -> int:
    fs = map(factorial, to_digits_stream(n))
    return sum(fs)
