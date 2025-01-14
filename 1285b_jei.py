"""
@file: 1285b_jei.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Just Eat It!(https://codeforces.com/problemset/problem/1285/B)
@version: 1.0
@date: 2025-01-14

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
        s = sum(a)
        pss = cls = crs = 0
        for i in range(n - 1):
            cls += a[i]
            crs += a[n - i - 1]
            pss = max(pss, max(cls, crs))
        print("YES" if s > pss else "NO")


if __name__ == "__main__":
    main()
