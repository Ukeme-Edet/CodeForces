"""
@file: 1759d_mir.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Make It Round(https://codeforces.com/problemset/problem/1759/D)
@version: 1.0
@date: 2024-12-13

@copyright: Copyright (c) 2024
"""

from math import lcm
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        res = n
        for i in range(19):
            if lcm(n, 10**i) // n <= m:
                res = lcm(n, 10**i) * (m // (lcm(n, 10**i) // n))
            else:
                break
        print(res)


if __name__ == "__main__":
    main()
