#!/usr/bin/env python3

import numpy
from math import sqrt
from printg import printg


primes = [
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157,
163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347,
349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439,
443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541
]


def mygen(max):
    '''Finds all primes up to <max> by appending each number up to <max>
    which has no factors from lesser primes.'''
    p = []
    for i in range(2, max + 1):
        for num in p:
            if i % num == 0:
                break
        else:
            p.append(i)
    return p


def esieve(num):
    '''Finds all primes in the range [2, <num>] via the Sieve of Erastothenes.'''
    a = numpy.full(num + 1, True)

    for i in range(2, int(sqrt(num)) + 1):
        if a[i]:
            for j in range(i**2, num + 1, i):
                a[j] = False

    primes = list()
    for i in range(2, num + 1):
        if a[i]:
            primes.append(i)

    return primes


if __name__ == '__main__':
    sieve = esieve(primes[-1])
    printg([
        num if num in esieve(primes[-1]) else 0
        for num in range(2, primes[-1] + 1)
    ])
    print('-' * 80)
    print(primes == sieve)
