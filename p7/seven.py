#!/usr/bin/env python3
import sys


def nthprime(n):
    primes = [2, 3, 5, 7, 11, 13]

    if n <= len(primes):
        return primes[n - 1]

    while len(primes) < n:
        x = primes[-1] + 1

        while True:
            for p in primes:
                if x % p == 0:
                    x += 1
                    break
            else:
                primes.append(x)
                break

    return primes[-1]


def main(argv):
    n = 10001
    try:
        n = int(argv[1])
    except (IndexError, ValueError):
        print(f'Usage: {argv[0]} n')
        print('\tfinds the nth prime number (n=10001 by default)')

    print(nthprime(n))


if __name__ == '__main__':
    main(sys.argv)
