"""
@file: 1890a_dp3.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Doremy's Paint 3(https://codeforces.com/problemset/problem/1890/A)
@version: 1.0
@date: 2025-06-29

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
        _ = int(input())
        v = list(Counter(int(x) for x in input().split()).values())
        print(
            "YES"
            if len(v) < 3
            and sum(abs(v[i] - v[i + 1]) for i in range(len(v) - 1)) < 2
            else "NO"
        )


if __name__ == "__main__":
    main()
