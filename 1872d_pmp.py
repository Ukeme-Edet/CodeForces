"""
@file: 1872d_pmp.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Plus Minus Permutation(https://codeforces.com/problemset/problem/1872/D)
@version: 1.0
@date: 2024-10-08

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
        n, x, y = [int(_) for _ in input().split()]
        xyl = lcm(x, y)
        nl, nx, ny = n // xyl, n // x, n // y
        nx -= nl
        ny -= nl
        print((nx * (2 * n - nx + 1)) // 2 - (ny * (2 + ny - 1)) // 2)


if __name__ == "__main__":
    main()
