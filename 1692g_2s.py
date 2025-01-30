"""
@file: 1692g_2s.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem 2^Sort(https://codeforces.com/problemset/problem/1692/G)
@version: 1.0
@date: 2025-01-30

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        n, k = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        res = 0
        i = 1
        while i < n:
            c = 1
            while i < n and a[i] << 1 > a[i - 1]:
                i += 1
                c += 1
            res += max(0, c - k)
            i += 1
        print(res)


if __name__ == "__main__":
    main()
