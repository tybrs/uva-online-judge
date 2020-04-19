import sys
import fileinput
import time
from functools import lru_cache, reduce

def memoize(f):
    '''Higher order function used as decorator to memoize
    outputs of lower order function.
    Input:
        f (function): function to memoize outputs
    Returns:
        function: helper function that memoizes
    output for new inputs of of some some lower order
    then outputs memoized output for lower order function.
    '''
    memo = {}
    def helper(x):
        if x not in memo:            
            memo[x] = f(x)
        return memo[x]
    return helper

def timeit(method):
    '''Higher order function used as decorator to print runtime
    of lower order function on completion
    '''
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print(f'{method.__name__}  {(te - ts) * 1000}')
        return result
    return timed
