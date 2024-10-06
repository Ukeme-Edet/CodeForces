"""
@file: 1931d_dp.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Divisible Pairs(https://codeforces.com/problemset/problem/1931/D)
@version: 1.0
@date: 2024-10-06

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
        n, x, y = [int(_) for _ in input().split()]
        a = [int(_) for _ in input().split()]
        sm = defaultdict(int)
        res = 0
        for ai in a:
            ix, iy = ai % x, ai % y
            yx = x - ix
            yx = 0 if yx == x else yx
            res += sm[f"{yx},{iy}"]
            sm[f"{ix},{iy}"] += 1
        print(res)


if __name__ == "__main__":
    main()
