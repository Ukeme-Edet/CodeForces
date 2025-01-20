"""
@file: 1077c_ga.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Good Array(https://codeforces.com/problemset/problem/1077/C)
@version: 1.0
@date: 2025-01-20

@copyright: Copyright (c) 2025
"""

from collections import defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    s = sum(a)
    fm = defaultdict(int)
    for ai in a:
        fm[ai] += 1
    res = []
    for i in range(n):
        s -= a[i]
        fm[a[i]] -= 1
        if not s % 2 and fm[s // 2] > 0:
            res.append(i + 1)
        s += a[i]
        fm[a[i]] += 1
    print(len(res))
    print(" ".join(str(x) for x in res))


if __name__ == "__main__":
    main()
