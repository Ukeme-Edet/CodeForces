"""
@file: 1513b_as.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem AND Sequences(https://codeforces.com/problemset/problem/1513/B)
@version: 1.0
@date: 2025-02-06

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def facMod(n, mod):
    res = 1
    for i in range(1, n + 1):
        res = (res * i) % mod
    return res


def main():
    for _ in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        bm = [0] * 31
        for i in a:
            for j in range(31):
                bm[j] += (i >> j) & 1
        edg = 0
        for i in a:
            edg += all(not (i >> j) & 1 or bm[j] == n for j in range(31))
        print(edg * (edg - 1) * facMod(n - 2, 10**9 + 7) % (10**9 + 7))


if __name__ == "__main__":
    main()
