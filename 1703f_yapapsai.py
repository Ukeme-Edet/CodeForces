"""
@file: 1703f_yapapsai.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Yet Another Problem About Pairs Satisfying an Inequality(https://codeforces.com/problemset/problem/1703/F)
@version: 1.0
@date: 2024-10-25

@copyright: Copyright (c) 2024
"""

from bisect import bisect_left
from collections import defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = sorted([(i + 1, int(x)) for i, x in enumerate(input().split())])
        sa = [0] * (n + 1)
        for i in range(n):
            sa[i + 1] = sa[i] + (1 if a[i][0] > a[i][1] else 0)
        res = 0
        for i in range(n):
            if a[i][0] > a[i][1]:
                res += sa[bisect_left(a, (a[i][1] - 1, float("inf")))]
        print(res)


if __name__ == "__main__":
    main()
