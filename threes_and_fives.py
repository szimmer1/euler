#!/usr/bin/env python

def largest_multiple(n, factor):
    # O(1)
    # returns the largest multiple less than n
    return n - 1 - ((n-1) % factor)

def multiple_sum_const(n, factor):
    m = largest_multiple(n, factor) / factor
    return factor / 2.0 * (m**2 + m)

def multiple_sum_linear(n, factor):
    return sum([i if i % factor == 0 else 0 for i in xrange(n)])

if __name__ == "__main__":
    assert multiple_sum_const(20,3) == 63
    assert multiple_sum_linear(20,3) == 63
