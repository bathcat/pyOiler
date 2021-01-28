from ..shared.digits import reverse_digits, is_palindrome
from ..shared.solver import Solver


def is_lychrel_candidate(n: int) -> bool:
    max_iterations = 50
    for i in range(0, max_iterations):
        n = n+reverse_digits(n)
        if is_palindrome(n):
            return False
    return True


def _solve(print=print):
    print('Is 47 a lychrel candidate? (Should be no.)')
    print(is_lychrel_candidate(47))


    print('Is 349 a lychrel candidate? (Should be no.)')
    print(is_lychrel_candidate(349))

    print('Is 196 a lychrel candidate? (Should be yes.)')
    print(is_lychrel_candidate(196))

    print("How many Lychrel candidates are there below ten-thousand?")
    ls = [i for i in range(10, 10000) if is_lychrel_candidate(i)]
    print(len(ls))

    print('And here they all are:')
    string_list = ', '.join([str(l) for l in ls])
    print('   ' + string_list)
    return True

description = '''If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?

NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.
'''

solver = Solver(55,
                'Lychrel numbers',
                description,
                _solve
                )



