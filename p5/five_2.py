#!/usr/bin/env python3
'''
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from sys import argv


def min_mul(num):
    result = 1
    l = list(reversed(range(2, num + 1)))

    while l:
        x = l.pop()
        for i, y in enumerate(l):
            if y % x == 0:
                l[i] = y // x
        result *= x

    return result


def check(num, x):
    for i in range(2, x + 1):
        if ( num % i ) != 0:
            return False
    return True


def main():
    if len(argv) == 3:
        num, x = int(argv[1]), int(argv[2])
        fmt = '{} {} divisible by every natural number up to {}'
        print(fmt.format(num, "is" if check(num, x) else "is not", x))

    elif len(argv) == 2:
        x = int(argv[1])
        print(f'{min_mul(x)} is divisible by every natural number up to {x}')

    else:
        print('Give one or two integers.')


if __name__ == '__main__':
    main()
