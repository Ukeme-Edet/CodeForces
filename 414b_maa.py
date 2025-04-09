"""
@file: 414b_maa.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Mashmokh and ACM(https://codeforces.com/problemset/problem/414/B)
@version: 1.0
@date: 2025-04-09

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


MOD = 10**9 + 7


def main():
    n, k = [int(x) for x in input().split()]
    fac = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            fac[j].append(i)
    nw = [[1] * (n + 1) for _ in range(k)]
    for i in range(1, k):
        for j in range(1, n + 1):
            nw[i][j] = sum(nw[i - 1][l] for l in fac[j]) % MOD
    print((sum(nw[-1]) - 1) % MOD)


if __name__ == "__main__":
    main()
