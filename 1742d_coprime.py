"""
@file: 1742d_coprime.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Coprime(https://codeforces.com/problemset/problem/1742/D)
@version: 1.0
@date: 2025-01-13

@copyright: Copyright (c) 2025
"""

from collections import defaultdict
from math import gcd
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        im = defaultdict(int)
        for i in range(n):
            im[a[i]] = i
        kv = list(im.items())
        res = 0
        for i in range(len(kv)):
            for j in range(len(kv)):
                if gcd(kv[i][0], kv[j][0]) == 1:
                    res = max(kv[i][1] + kv[j][1], res)
        print(res + 2 if res else -1)


if __name__ == "__main__":
    main()
