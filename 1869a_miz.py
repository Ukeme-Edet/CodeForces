"""
@file: 1869a_miz.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Make It Zero(https://codeforces.com/problemset/problem/1869/A)
@version: 1.0
@date: 2025-02-06

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n = int(input())
        _ = [int(x) for x in input().split()]
        print(4)
        print(1, n)
        print(1, (n // 2) * 2)
        print(n - 1, n)
        print(n - 1, n)


if __name__ == "__main__":
    main()
