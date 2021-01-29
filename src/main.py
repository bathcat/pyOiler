import time
import cProfile


from pyoiler.problems.euler021 import solver


class Colors:
    Red = '\033[91m'
    Green = '\033[92m'
    Normal = '\033[0m'


class Messages:
    passed = f"{Colors.Green}Passed{Colors.Normal}"
    failed = f"{Colors.Red}Failure{Colors.Normal}"
    exception = f"{Colors.Red}[[Exception]]{Colors.Normal}"


def execute():
    start = time.time()

    print('-------------------------------------------------')
    print(f"Number: {solver.id}")
    print(f"Name: {solver.name}")
    print(f"Uri: {solver.uri}")
    print('Description: ')
    [print('   ' + l) for l in solver.description.splitlines()]
    print()

    print('Output: ')

    passed = False
    # try:
    passed = solver.solve(lambda x: print('  ' + str(x)))
    # except:
    #     #print(Messages.exception)
    #     pass

    complete = time.time()

    print()
    print(f"Result: {Messages.passed if passed else Messages.failed}")

    print(f'Elapsed (s): {complete - start}')

    print('---------------------------------------------------')



def profile():
    cProfile.run('solver.solve()')



if __name__ == '__main__':
    execute()
