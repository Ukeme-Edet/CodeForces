"""
@file: 1183d_cb.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Candy Box (easy version)(https://codeforces.com/problemset/problem/1183/D)
@version: 1.0
@date: 2025-03-11

@copyright: Copyright (c) 2025
"""

from collections import Counter, defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n = int(input())
        a = Counter(int(x) for x in input().split())
        fm = defaultdict(int, Counter(a.values()))
        v = list(a.values())
        for i in range(len(v)):
            while fm[v[i]] > 1 and v[i] > 0:
                fm[v[i]] -= 1
                v[i] -= 1
                fm[v[i]] += 1
        print(sum(v))


if __name__ == "__main__":
    main()
