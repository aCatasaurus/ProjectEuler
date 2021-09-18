#!/usr/bin/env python3

# Find the largest palindrome made from the product of two 3-digit numbers.

# brute force method

def is_palindrome(num):
    s = str(num)
    for i in range(0, len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True

def palindromes(digits, base=10):
    t = 0
    for a in reversed(range(base**(digits - 1), base**digits)):
        if a < t:
            break
        for b in reversed(range(base**(digits - 1), base**digits)):
            if is_palindrome(a * b):
                t = b
                yield a, b
                break

def largest_palindrome(digits, base=10):
    return max(palindromes(digits, base), key=lambda pair: pair[0] * pair[1])

# end brute force method

def p(digits, base=10):
    a = [base - 1] * digits
    b = [base - 1] * digits

if __name__ == '__main__':
    a, b = largest_palindrome(3)
    print(a, '*', b, '=', a * b)
