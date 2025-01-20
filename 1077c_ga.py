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
    em = defaultdict(list)
    for i in range(n):
        em[a[i]].append(i)
    res = set()
    for i in range(n):
        if em[s - a[i] * 2]:
            [res.add(x) for x in em[s - a[i] * 2] if x != i]
    print(len(res))
    print(" ".join(str(x + 1) for x in res))


if __name__ == "__main__":
    main()
