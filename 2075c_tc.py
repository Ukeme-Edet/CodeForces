"""
@file: 2075c_tc.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Two Colors(https://codeforces.com/contest/2075/problem/C)
@version: 1.0
@date: 2025-03-17

@copyright: Copyright (c) 2025
"""

from bisect import bisect_left
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n, m = [int(x) for x in input().split()]
        a = sorted(int(x) for x in input().split())
        psa = [0] * (m + 1)
        for i in range(m):
            a[i] = n - 1 if a[i] >= n else a[i]
            psa[i + 1] = psa[i] + a[i]
        res = 0
        for i in range(m):
            idx = bisect_left(a, n - a[i])
            res += (
                psa[i] - psa[idx] - (i - idx) * (n - a[i] - 1)
                if idx < i
                else 0
            )
        print(res * 2)


if __name__ == "__main__":
    main()
