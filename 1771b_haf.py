"""
@file: 1771b_haf.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Hossam and Friends(https://codeforces.com/problemset/problem/1771/B)
@version: 1.0
@date: 2024-12-11

@copyright: Copyright (c) 2024
"""

from collections import defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        sd = defaultdict(int)
        for _ in range(m):
            x, y = sorted(int(x) for x in input().split())
            sd[y] = max(sd[y], x)
        l = r = 1
        res = 0
        while r <= n:
            l = max([sd[r], l - 1]) + 1
            res += r - l + 1
            r += 1
        print(res)


if __name__ == "__main__":
    main()
