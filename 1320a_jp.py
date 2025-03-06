"""
@file: 1320a_jp.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Journey Planning(https://codeforces.com/problemset/problem/1320/A)
@version: 1.0
@date: 2025-03-06

@copyright: Copyright (c) 2025
"""

from collections import defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    n = int(input())
    b = [int(x) for x in input().split()]
    bm = defaultdict(int)
    for i in range(n):
        bm[str(i - b[i])] += b[i]
    print(max(bm.values()))


if __name__ == "__main__":
    main()
