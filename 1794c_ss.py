"""
@file: 1794c_ss.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Scoring Subsequences(https://codeforces.com/problemset/problem/1794/C)
@version: 1.0
@date: 2024-10-21

@copyright: Copyright (c) 2024
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        cr, l, r = 1, 0, 0
        res = [0] * n
        while r < n:
            cr *= a[r]
            cr /= r - l + 1
            while a[l] < r - l + 1:
                cr /= a[l]
                cr *= r - l + 1
                l += 1
            res[r] = r - l + 1
            r += 1
        print(" ".join([str(x) for x in res]))


if __name__ == "__main__":
    main()
