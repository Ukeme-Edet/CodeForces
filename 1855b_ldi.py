"""
@file: 1855b_ldi.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Longest Divisors Interval(https://codeforces.com/problemset/problem/1855/B)
@version: 1.0
@date: 2025-02-07

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n = int(input())
        d = 1
        while not n % d:
            d += 1
        print(d - 1)


if __name__ == "__main__":
    main()
