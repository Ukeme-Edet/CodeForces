"""
@file: 1631b_fwes.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Fun with Even Subarrays(https://codeforces.com/problemset/problem/1631/B)
@version: 1.0
@date: 2025-01-24

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
        a = [int(_) for _ in input().split()]
        ans = 0
        lc, i = 0, n - 1
        while i >= 0:
            if a[i] == a[-1]:
                lc += 1
                i -= 1
            else:
                ans += 1
                i -= lc
                lc = n - i - 1
        print(ans)


if __name__ == "__main__":
    main()
