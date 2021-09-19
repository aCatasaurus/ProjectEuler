#!/usr/bin/env python3
'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def check(a, b, c, verbose=False):
    d = a**2 + b**2 - c**2
    if verbose:
        print(f'{a:>3}^2 + {b:>3}^2 - {c:>3}^2 -> {d:> 7}')
    return d == 0


def find(verbose=False):
    s = 1000

    for a in range(1, (s - 3) // 3 + 1):
        a2 = a**2
        for b in range(a + 1, (s - a - 1) // 2 + 1):
            c = 1000 - a - b

            if check(a, b, c, verbose):
                return a, b, c


def main():
    a, b, c = find()
    print(f'The triple is ({a}, {b}, {c}) with abc = {a*b*c}')


if __name__ == '__main__':
    main()
