"""
@file: 2055b_crafting.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Crafting(https://codeforces.com/contest/2055/problem/B)
@version: 1.0
@date: 2025-01-12

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        print(
            "YES"
            if sum([a[i] < b[i] for i in range(n)]) <= 1
            and min([a[i] - b[i] for i in range(n) if a[i] >= b[i]], default=0)
            >= sum([b[i] - a[i] for i in range(n) if b[i] > a[i]])
            else "NO"
        )


if __name__ == "__main__":
    main()
