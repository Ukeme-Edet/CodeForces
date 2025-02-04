"""
@file: 1438b_vae.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Valerii Against Everyone(https://codeforces.com/problemset/problem/1438/B)
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
        n = int(input())
        a = set([int(x) for x in input().split()])
        print("YES" if len(a) != n else "NO")


if __name__ == "__main__":
    main()
