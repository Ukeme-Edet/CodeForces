"""
@file: 1475c_bib.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Ball in Berland(https://codeforces.com/problemset/problem/1475/C)
@version: 1.0
@date: 2025-02-08

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout
from collections import Counter


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        _, _, k = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        ab = zip(a, b)
        afm, bfm = Counter(a), Counter(b)
        res = 0
        for u, v in ab:
            res += k - afm[u] - bfm[v] + 1
        print(res // 2)


if __name__ == "__main__":
    main()
