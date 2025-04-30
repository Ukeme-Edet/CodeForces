"""
@file: 1665b_act.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Array Cloning Technique(https://codeforces.com/problemset/problem/1665/B)
@version: 1.0
@date: 2025-04-30

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout
from typing import Counter


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        fc = Counter([str(x) for x in a])
        td = sorted(fc.values())[-1]
        res = n - td
        while td < n:
            res += 1
            td *= 2
        print(res)


if __name__ == "__main__":
    main()
