"""
@file: 2031a_pamm.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Penchick and Modern Monument(https://codeforces.com/contest/2031/problem/A)
@version: 1.0
@date: 2024-11-17

@copyright: Copyright (c) 2024
"""

from collections import Counter
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        fm = Counter([x for x in input().split()])
        print(n - max(fm.values()))


if __name__ == "__main__":
    main()
