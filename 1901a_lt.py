"""
@file: 1901a_lt.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Line Trip(https://codeforces.com/problemset/problem/1901/A)
@version: 1.0
@date: 2025-04-30

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n, x = [int(x) for x in input().split()]
        a = [0] + [int(x) for x in input().split()]
        print(
            max(max(a[i] - a[i - 1] for i in range(1, n + 1)), (x - a[-1]) * 2)
        )


if __name__ == "__main__":
    main()
