"""
@file: 1374d_zra.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Zero Remainder Array(https://codeforces.com/problemset/problem/1374/D)
@version: 1.0
@date: 2025-02-08

@copyright: Copyright (c) 2025
"""

from collections import Counter
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n, k = [int(x) for x in input().split()]
        mfm = Counter([k - int(x) % k for x in input().split() if int(x) % k])
        res = 0
        for key, v in mfm.items():
            res = max(key + 1 + k * (v - 1), res)
        print(res)


if __name__ == "__main__":
    main()
