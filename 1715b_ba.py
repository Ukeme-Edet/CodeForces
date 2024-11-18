"""
@file: 1715b_ba.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Beautiful Array(https://codeforces.com/contest/1715/problem/B)
@version: 1.0
@date: 2024-11-19

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
        n, k, b, s = [int(x) for x in input().split()]
        if k * b > s or (k - 1) * (n - 1) < s - k * (b + 1) + 1:
            print(-1)
            continue
        res = [0] * n
        res[0], s = min(k * (b + 1) - 1, s), s - min(k * (b + 1) - 1, s)
        for i in range(1, n):
            res[i], s = min(s, k - 1), s - min(s, k - 1)
        print(" ".join(str(x) for x in res))


if __name__ == "__main__":
    main()
