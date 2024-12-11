"""
@file: 1601a_ae.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Array Elimination(https://codeforces.com/problemset/problem/1601/A)
@version: 1.0
@date: 2024-12-11

@copyright: Copyright (c) 2024
"""

from math import gcd
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
        bcl = [0] * 30
        for ai in a:
            for i in range(30):
                bcl[i] += (ai >> i) & 1
        res = 0
        for i in range(30):
            res = gcd(res, bcl[i])
        print(
            " ".join(
                [str(x) for x in range(1, n + 1) if not res % x]
                if res
                else [str(x) for x in range(1, n + 1)]
            )
        )


if __name__ == "__main__":
    main()
