from typing import Callable
from dataclasses import dataclass

t_print = Callable[[str], None]
t_solve = Callable[[t_print], bool]

@dataclass(frozen=True)
class Solver():
    id: int
    name: str
    description: str
    solve: t_solve

    @property
    def uri(self):
        return f'https://projecteuler.net/problem={self.id}'

