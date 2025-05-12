"""
@file: 279b_books.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Books(https://codeforces.com/contest/279/problem/B)
@version: 1.0
@date: 2025-05-12

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    n, t = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    l = r = res = cb = 0
    while r < n:
        if cb + a[r] <= t:
            cb += a[r]
            r += 1
        else:
            cb -= a[l]
            l += 1
        res = max(res, r - l)
    print(res)


if __name__ == "__main__":
    main()
