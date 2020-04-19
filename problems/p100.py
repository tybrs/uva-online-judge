
import fileinput
from functools import lru_cache

@lru_cache(maxsize=None)
def collatz_length(n):
    '''Given a integer ``n`` as input calculate the cycle length
    of the Collatz sequence starting that begins with n.

    Performance increased by adding memoizing cache on recursive
    faction calls.

    Inputs:
        n (int): The Collatz sequence beginning with n.
    Returns:
        int: The cycle length of the Collatz sequence
    starting at n.
    '''
    if n < 1:
        return 0
    if n == 1:
        return 1
    elif n % 2 != 0:
        return 1 +  collatz_length(3 * n + 1)
    else:
        return 1 +  collatz_length(n // 2)

@timeit
@lru_cache(maxsize=None)
def max_length(start, end):
    '''Compute max cycle length for all Collatz sequences
    between ``i`` and ``j``.
    Inputs:
        i (int) : lower bound of Collatz sequences to compute
        j (int) : upper bound of Collatz sequences to compute
    Returns:
        int: the maxim cycle length ``m`` for all Collatz
    sequences between ``i`` and ``j``.
    '''
    start, end = min(start, end), max(start, end)
    return max(map(collatz_length, range(start, end + 1)))


def main():
    for line in fileinput.input():
        start, end = map(int, line.split())
        print(start, end, max_length(start, end))

if __name__ == '__main__':
    main()
    exit(0)
