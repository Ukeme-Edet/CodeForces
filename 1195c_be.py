"""
@file: 1195c_be.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Basketball Exercise(https://codeforces.com/problemset/problem/1195/C)
@version: 1.0
@date: 2025-03-07

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
    h1 = [int(x) for x in input().split()]
    h2 = [int(x) for x in input().split()]
    rt = [[0, 0, 0] for i in range(n)]
    rt[-1] = [h1[-1], h2[-1], 0]
    for i in range(n - 2, -1, -1):
        rt[i] = [
            h1[i] + max(rt[i + 1][1], rt[i + 1][2]),
            h2[i] + max(rt[i + 1][0], rt[i + 1][2]),
            max(rt[i + 1]),
        ]
    print(max(rt[0]))


if __name__ == "__main__":
    main()
