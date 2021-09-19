#!/usr/bin/env python3
'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

# import esieve from ../primes.py
import sys
sys.path.insert(0, '..')
from primes import esieve


def sumprimesupto(n):
    return sum(esieve(n))


if __name__ == '__main__':
    print(sumprimesupto(2000000))
