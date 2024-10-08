"""
@file: 1904b_cg.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Collecting Game(https://codeforces.com/problemset/problem/1904/B)
@version: 1.0
@date: 2024-10-08

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
        n = int(input())
        a = sorted([(int(x), i) for i, x in enumerate(input().split())])
        psa = [0] * (n + 1)
        for i in range(n):
            psa[i + 1] = psa[i] + a[i][0]
        res = [0] * n
        i = 0
        while i < n:
            cs = psa[i + 1]
            j = i
            i += 1
            while i < n and a[i][0] <= cs:
                cs += a[i][0]
                i = bisect_left(psa, cs)
            while j < i:
                res[a[j][1]] = i - 1
                j += 1
        print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()
