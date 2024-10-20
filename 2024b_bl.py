"""
@file: 2024b_bl.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Buying Lemonade(https://codeforces.com/contest/2024/problem/B)
@version: 1.0
@date: 2024-10-20

@copyright: Copyright (c) 2024
"""

from bisect import bisect_left
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        a = sorted([int(x) for x in input().split()])
        vals = sorted(set(a))
        ps = ks = i = ib = ln = 0
        while ks < k:
            ki = bisect_left(a, vals[i])
            ps += ki - ib
            ib = ki
            ps += min(k - ks, (vals[i] - ln) * (n - ki))
            ks += min(k - ks, (vals[i] - ln) * (n - ki))
            ln = vals[i]
            i += 1
        print(ps)


if __name__ == "__main__":
    main()
