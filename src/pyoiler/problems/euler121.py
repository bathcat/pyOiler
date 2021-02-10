from ..shared.solver import Solver
import enum
import math
import random
import dataclasses
from typing import Iterable
from fractions import Fraction

import multiprocessing as mp

import rx
from rx import operators as ops

"""[summary]

An actual solution would look like this:

    result =  \
              Fraction(1,2) * Fraction(1,3) * Fraction(1,4) * Fraction(1,5) \
            + Fraction(1,2) * Fraction(1,3) * Fraction(1,4) * Fraction(4,5) \
            + Fraction(1,2) * Fraction(1,3) * Fraction(1,4) * Fraction(1,5) \
            + Fraction(1,2) * Fraction(2,3) * Fraction(1,4) * Fraction(1,5) \
            + Fraction(1,2) * Fraction(1,3) * Fraction(3,4) * Fraction(1,5) \

""" 


@enum.unique
class Color(enum.Enum):
    Red=enum.auto()
    Blue=enum.auto()

@enum.unique
class Outcome(enum.Enum):
    Loss=enum.auto()
    Win=enum.auto()

class Bag:
    def __init__(self) -> None:
        self._contents = [Color.Red,Color.Blue]
    
    def draw(self)->Color:
        result = random.choice(self._contents)
        self._contents.append(Color.Red)
        return result



@dataclasses.dataclass(frozen=True)
class Game:
    picks:Iterable[Color]

    @property
    def outcome(self)->Outcome:
        blue_picks = len([1 for p in self.picks if p==Color.Blue])
        return Outcome.Win if blue_picks > (len(self.picks)//2) else Outcome.Loss

    def __str__(self) -> str:
        return f'{self.outcome.name} ({[pick.name for pick in self.picks]})'


def play(turns:int)->Game:
    if turns < 1:
        raise ValueError("Turns must be a positive number")

    bag = Bag()
    picks = [bag.draw() for _ in range(turns) ]
    
    return Game(picks)

def play_w(turns:int)->bool:
    bag = Bag()
    picks = [bag.draw() for _ in range(turns) ]
    blues = len([1 for p in picks if p==Color.Blue])
    
    return blues > (turns//2)


def _solve_naive(print=print):
    print(f'\n\n\n***************')
    
    turns=15
    game_count=150_000_000
    wins=0

    for i in range(game_count):
        game = play(turns)
        if game.outcome==Outcome.Win:
            wins+=1

    print(f'  Max prize: {math.floor(game_count/wins)}')

    print(f"Not done")
    return False

def _solve_rx(print=print):
    """Benchmark: 15/1_000_000 takes 30s """
    print(f'\n\n\n***************')
    
    turns=15
    game_count=1_000_000

    #scheduler=rx.scheduler.CurrentThreadScheduler()
    scheduler=rx.scheduler.ThreadPoolScheduler(4)

    wins = rx.range(0,game_count,scheduler=scheduler)\
             .pipe(
                 ops.filter(lambda i: play_w(turns)),
                 ops.count()
             ).run()


    print(f'  Max prize: {math.floor(game_count/wins)}')

    print(f"Not done")
    return False

turns=15

def do_play(throwaway:int)->bool:
    bag = Bag()
    picks = [bag.draw() for _ in range(turns) ]
    blues = len([1 for p in picks if p==Color.Blue])
    return blues > (turns//2)


def _solve(print=print):
    """Benchmark: 15/1_000_000 takes 4s """
    print(f'\n\n\n***************')
    
    game_count=250_000_000
    wins = 0
    with mp.Pool(12) as pool:
        results = pool.map(do_play, range(game_count),5_000)
        wins = len([r for r in results if r])

    print(f'  Max prize: {math.floor(game_count/wins)}')

    print(f"Not done")
    return False


description = '''
A bag contains one red disc and one blue disc. In a game of chance a player 
takes a disc at random and its colour is noted. After each turn the disc is 
returned to the bag, an extra red disc is added, and another disc is taken 
at random.

The player pays £1 to play and wins if they have taken more blue discs than 
red discs at the end of the game.

If the game is played for four turns, the probability of a player winning is 
exactly 11/120, and so the maximum prize fund the banker should allocate for 
winning in this game would be £10 before they would expect to incur a loss. 
Note that any payout will be a whole number of pounds and also includes the 
original £1 paid to play the game, so in the example given the player actually 
wins £9.

Find the maximum prize fund that should be allocated to a single game in which 
fifteen turns are played.

'''

solver = Solver(121,
                'Disc game prize fund',
                description,
                _solve
                )
