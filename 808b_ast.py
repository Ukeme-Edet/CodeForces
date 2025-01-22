"""
@file: 808b_ast.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Average Sleep Time(https://codeforces.com/problemset/problem/808/B)
@version: 1.0
@date: 2025-01-22

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, k = [int(_) for _ in input().split()]
    a = [int(_) for _ in input().split()]
    cs = 0
    for i in range(k):
        cs += a[i]
    ans = cs
    for i in range(k, n):
        cs += a[i] - a[i - k]
        ans += cs
    print("{:.6f}".format(ans / (n - k + 1)))


if __name__ == "__main__":
    main()
