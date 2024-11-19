"""
@file: 1827a_co.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Counting Orders(https://codeforces.com/problemset/problem/1827/A)
@version: 1.0
@date: 2024-11-19

@copyright: Copyright (c) 2024
"""

from bisect import bisect_left
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = sorted(int(x) for x in input().split())
        b = sorted(int(x) for x in input().split())
        res = 1
        for i in range(n):
            j = bisect_left(b, a[i])
            res *= j - i
            res %= 1000000007
        print(res)


if __name__ == "__main__":
    main()
