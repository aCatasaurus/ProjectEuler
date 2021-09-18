#!/usr/bin/env python3

# What is the largest prime factor of the number 600851475143 ?

from math import sqrt

def max_factor(num):
    i = 2
    root = int(sqrt(num))
    while i <= root:
        if num == i:
            break
        elif num % i == 0:
            num = num // i
        else:
            i += 1
    return num

if __name__ == '__main__':
    print(max_factor(600851475143))
