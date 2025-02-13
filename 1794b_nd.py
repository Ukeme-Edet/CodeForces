"""
@file: 1794b_nd.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Not Dividing(https://codeforces.com/contest/1794/problem/B)
@version: 1.0
@date: 2025-02-13

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
        a = [int(x) if x != "1" else 2 for x in input().split()]
        for i in range(n - 1):
            if not a[i + 1] % a[i]:
                a[i + 1] += 1
        print(*a)


if __name__ == "__main__":
    main()
