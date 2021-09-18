#!/usr/bin/env python3
'''
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

from sys import argv


class Factors:
    def __init__(self, num):
        self.set = set()
        self.counts = dict()
        self.update(num)

    def product(self):
        p = 1
        for i in self.set:
            p *= i ** self.counts[i]
        return p

    def update(self, num):
        for i in range(2, num + 1):
            if num % i == 0:
                if i not in self.set:
                    self.set.add(i)
                    self.counts[i] = 0
                count = 0
                while num % i == 0:
                    count += 1
                    num //= i
                if count > self.counts[i]:
                    self.counts[i] = count

    def __or__(self, other):
        n = Factors(1)
        n.set = self.set | other.set
        for i in n.set:
            n.count[i] = max(self.count[i], self.other[i])
        return n


def min_mul(num):
    factors = Factors(num)
    for i in range(num - 1, 1, -1):
        if ( num % i ) != 0:
            factors.update(i)
    return factors.product()


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
