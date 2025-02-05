"""
@file: 1418a_bt.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Buying Torches(https://codeforces.com/problemset/problem/1418/A)
@version: 1.0
@date: 2025-02-05

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        x, y, k = [int(x) for x in input().split()]
        print(((y + 1) * k + x - 3) // (x - 1) + k)


if __name__ == "__main__":
    main()
