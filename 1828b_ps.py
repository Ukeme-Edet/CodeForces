"""
@file: 1828b_ps.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Permutation Swap(https://codeforces.com/problemset/problem/1828/B)
@version: 1.0
@date: 2025-02-07

@copyright: Copyright (c) 2025
"""

from math import gcd
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n = int(input())
        p = [int(x) for x in input().split()]
        res = p[0] - 1
        for i in range(n):
            res = gcd(res, p[i] - i - 1)
        print(res)


if __name__ == "__main__":
    main()
