#!/usr/bin/env python

# Find the sum of even fibonacci numbers in range [1,N], 
# where N is in [10, 4e16]

def recursive_fib(i):
    if i == 0:
        return 1
    elif i == 1:
        return 2
    else:
        return recursive_fib(i-2) + recursive_fib(i-1)

def recursive_fib_gen_no_memo(N):
    # using textbook recursive fib solution
    # S = O(1), unless taking stack frames into account
    # T = O(2^n), where n is number if fibs generated
    i = 0
    while True:
        f = recursive_fib(i)
        if f <= N:
            yield f
        else:
            break
        i = i + 1

def fib_gen(N):
    # infinitely generates fibonacci numbers, i.e. not using a target index
    # S = O(1)
    # T = O(n)
    low, high = 1, 2
    yield low
    yield high
    while True:
        low, high = high, low + high
        if high > N:
            break
        yield high

def even_fib(N):
    _sum = 0
    for f in fib_gen(N):
        if f % 2 == 0:
            _sum = _sum + f
    return _sum

if __name__ == "__main__":
    n_tests = int(raw_input())
    for _ in xrange(n_tests):
        print even_fib(long(raw_input()))
