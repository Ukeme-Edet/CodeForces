"""
@file: 1420b_ral.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Rock and Lever(https://codeforces.com/problemset/problem/1420/B)
@version: 1.0
@date: 2025-01-23

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout
from collections import Counter


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        _ = int(input())
        print(
            sum(
                (x * (x - 1)) // 2
                for x in Counter(
                    int(x).bit_length() for x in input().split()
                ).values()
            )
        )


if __name__ == "__main__":
    main()
