"""
@file: 1119b_aaanf.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Alyona and a Narrow Fridge(https://codeforces.com/problemset/problem/1119/B)
@version: 1.0
@date: 2025-01-17

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, h = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    for i in range(n):
        ta = sorted(a[: i + 1])
        s = 0
        for j in range(len(ta) % 2, len(ta), 2):
            s += max(ta[j], ta[j + 1])
        s += ta[0] if len(ta) % 2 else 0
        if s > h:
            print(i)
            break
    else:
        print(n)


if __name__ == "__main__":
    main()
