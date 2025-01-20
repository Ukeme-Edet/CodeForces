"""
@file: 1682b_ands.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem AND Sorting(https://codeforces.com/problemset/problem/1682/B)
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
    for _ in range(int(input())):
        n = int(input())
        p = [int(x) for x in input().split()]
        res = 2**31 - 1
        for i in range(n):
            if p[i] != i:
                res &= p[i]
        print(res)


if __name__ == "__main__":
    main()
