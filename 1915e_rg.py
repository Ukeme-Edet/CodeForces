"""
@file: 1915e_rg.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Romantic Glasses(https://codeforces.com/problemset/problem/1915/E)
@version: 1.0
@date: 2024-10-08

@copyright: Copyright (c) 2024
"""

from collections import defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(_) for _ in input().split()]
        psa = [0] * (n + 1)
        for i in range(n):
            psa[i + 1] = psa[i] + a[i] if i % 2 else psa[i] - a[i]
        psa.sort()
        for i in range(n):
            if psa[i] == psa[i + 1]:
                print("YES")
                break
        else:
            print("NO")


if __name__ == "__main__":
    main()
