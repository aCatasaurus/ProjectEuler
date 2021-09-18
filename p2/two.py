#!/usr/bin/env python3

# By considering the terms in the Fibonacci sequence
# whose values do not exceed four million,
# find the sum of the even-valued terms.


def gen_fib():
    sum = 1
    last = 0
    temp = 0
    while True:
        yield sum
        temp = sum
        sum += last
        last = temp

def do():
    sum = 0
    g = gen_fib()
    a = next(g)
    while a < 1000000:
        if a % 2 == 0:
            sum += a
        a = next(g)
    return sum

if __name__ == '__main__':
    print(do())
