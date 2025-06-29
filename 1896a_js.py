"""
@file: 1896a_js.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Jagged Swaps(https://codeforces.com/problemset/problem/1896/A)
@version: 1.0
@date: 2025-06-29

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
        a = [int(x) for x in input().split()]
        print("YES" if a[0] == 1 else "NO")


if __name__ == "__main__":
    main()
