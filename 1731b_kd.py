"""
@file: 1731b_kd.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Kill Demodogs(https://codeforces.com/problemset/problem/1731/B)
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
        n = int(input())
        MOD = 10**9 + 7
        res = n * (n + 1) * (4 * n - 1) // 6
        print((res * 2022) % MOD)


if __name__ == "__main__":
    main()
