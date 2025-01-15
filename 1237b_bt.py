"""
@file: 1237b_bt.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Balanced Tunnel(https://codeforces.com/problemset/problem/1237/B)
@version: 1.0
@date: 2025-01-15

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
    b = [int(x) for x in input().split()]
    seen = defaultdict(int)
    res = 0
    i = j = 0
    while j < n:
        if seen[a[i]]:
            i += 1
        elif a[i] == b[j]:
            i += 1
            j += 1
        else:
            seen[b[j]] += 1
            j += 1
            res += 1
    print(res)


if __name__ == "__main__":
    main()
