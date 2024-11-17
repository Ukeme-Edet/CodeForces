"""
@file: 1725b_bt.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Basketball Together(https://codeforces.com/problemset/problem/1725/B)
@version: 1.0
@date: 2024-11-17

@copyright: Copyright (c) 2024
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, d = [int(x) for x in input().split()]
    p = sorted([int(x) for x in input().split()])
    res = cp = i = 0
    while n:
        cp += p[-i - 1]
        n -= 1
        if cp > d:
            cp = 0
            i += 1
            res += 1
    print(res)


if __name__ == "__main__":
    main()
