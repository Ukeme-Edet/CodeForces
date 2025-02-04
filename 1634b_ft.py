"""
@file: 1634b_ft.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Fortune Telling(https://codeforces.com/problemset/problem/1634/B)
@version: 1.0
@date: 2025-02-04

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep="", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n, x, y = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        print("Alice" if (x + sum(a)) % 2 == y % 2 else "Bob")


if __name__ == "__main__":
    main()
