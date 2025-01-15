"""
@file: 1514b_a0db.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem AND 0, Sum Big(https://codeforces.com/problemset/problem/1514/B)
@version: 1.0
@date: 2025-01-15

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        MOD = 10**9 + 7
        res = 1
        for _ in range(k):
            res = (res * n) % MOD
        print(res)


if __name__ == "__main__":
    main()
