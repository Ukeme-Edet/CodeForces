"""
@file: 1701c_sm.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Schedule Management(https://codeforces.com/problemset/problem/1701/C)
@version: 1.0
@date: 2025-01-30

@copyright: Copyright (c) 2025
"""

from collections import Counter, defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        n, m = [int(x) for x in input().split()]
        fma = {str(i): 0 for i in range(1, n + 1)}
        fma.update(Counter(x for x in input().split()))
        l, r = 0, m * 2 + 1
        res = float("inf")
        while l < r:
            t = l + ((r - l) >> 1)
            cp, ic = 0, 0
            for v in fma.values():
                cp += min(t, v) + ((t - min(t, v)) >> 1)
            if cp >= m:
                res = min(res, t)
                r = t
            else:
                l = t + 1
        print(res)


if __name__ == "__main__":
    main()
