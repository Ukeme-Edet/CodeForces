"""
@file: 1350b_oam.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Orac and Models(https://codeforces.com/problemset/problem/1350/B)
@version: 1.0
@date: 2025-02-09

@copyright: Copyright (c) 2025
"""

from collections import defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    fm = defaultdict(list)
    for i in range(1, 100001):
        for j in range(i, 100001, i):
            fm[str(j)].append(i)
    for _ in range(int(input())):
        n = int(input())
        s = [int(x) for x in input().split()]
        dp = [0] * (n + 1)
        for i in range(n, 0, -1):
            for j in fm[str(i)]:
                if s[i - 1] > s[j - 1]:
                    dp[j] = max(dp[j], dp[i] + 1)
        print(max(dp) + 1)


if __name__ == "__main__":
    main()
