"""
@file: 1826b_lnc.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Lunatic Never Content(https://codeforces.com/problemset/problem/1826/B)
@version: 1.0
@date: 2024-12-01

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
        res = abs(a[0] - a[-1])
        for i in range(n // 2):
            res = gcd(res, abs(a[i] - a[-i - 1]))
        print(res)


if __name__ == "__main__":
    main()
