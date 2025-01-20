"""
@file: 1497b_ma.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem M-arrays(https://codeforces.com/problemset/problem/1497/B)
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
    for _ in range(int(input())):
        n, m = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        d = defaultdict(int)
        for i in range(n):
            d[a[i] % m] += 1
        res = 0
        for i in range(1, (m + 1) // 2):
            if d[i] or d[m - i]:
                res += 1
                res += max(0, abs(d[i] - d[m - i]) - 1)
        res += d[0] > 0
        res += not m % 2 and d[m // 2] > 0
        print(res)


if __name__ == "__main__":
    main()
