"""
@file: 2025b_bcko.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Binomial Coefficients, Kind Of(https://codeforces.com/contest/2025/problem/B)
@version: 1.0
@date: 2024-10-14

@copyright: Copyright (c) 2024
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    _ = int(input())
    pcd = {}
    r, MOD = 1, 1000000007
    for i in range(1, 100001):
        r *= 2
        r %= MOD
        pcd[i] = r
    n, k = [int(x) for x in input().split()], [int(x) for x in input().split()]
    for ki in k:
        print(pcd[ki])


if __name__ == "__main__":
    main()
