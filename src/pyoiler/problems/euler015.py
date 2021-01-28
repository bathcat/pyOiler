from typing import Iterable, Tuple
from ..shared.more_itertools import flat_map, count
from ..shared.solver import Solver

"""[summary]
2 thoughts on performance:
    1. This *enumerates* paths, which isn't necessary.
        All we need to do is count them, so just increment
        a number when you get to 16,16, and forget about
        holding on to the tail.
    2. Adding threads should be trivial, especially
        after changing the search to depth-first.

Returns:
[type]: [description]

Yields:
[type]: [description]
"""

Position = Tuple[int,int]

class Path():
    head:Position
    tail: 'Path'
    def __init__(self, end:Position, rest:'Path' = None):
        self.head = end
        self.tail = rest

    def to_positions(self) -> Iterable[Position]:
        yield self.head
        if self.tail:
            yield from self.tail.to_positions()

    def append(self, p:Position) -> 'Path':
        return Path(p, self)

    def __str__(self):
        ps = list(self.to_positions())
        ps.reverse()
        return str(ps)

    @classmethod
    def zero(cls) -> 'Path':
        return Path((0,0))

class Lattice():
    height:int
    width:int
    def __init__(self,width, height):
        self.width=width
        self.height=height

    def successor_paths(self, current:Path) -> Iterable[Path]:
        if current.head[0] < self.width:
            yield current.append((current.head[0] + 1, current.head[1]))
        if current.head[1] < self.height:
            yield current.append((current.head[0], current.head[1] + 1))

    def paths(self) -> Iterable[Path]:
        partials = [Path.zero()]

        for _ in range(self.height + self.width):
            partials = flat_map(self.successor_paths, partials)

        return partials


def _solve(print = print):
    side = 15
    l = Lattice(side,side)
    path_count = count(l.paths())
    print(f"Count of paths through a {side} lattice is: {path_count}")
    print('This approach doesn''t scale.')
    return False




description = '''Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner. 

How many such routes are there through a 20×20 grid?
'''

solver = Solver(15,
                'Lattice paths',
                description,
                _solve
                )
