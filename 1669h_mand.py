"""
@file: 1669h_mand.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Maximal AND(https://codeforces.com/problemset/problem/1669/H)
@version: 1.0
@date: 2024-11-20

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
        n, k = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        bfm = defaultdict(int)
        res = a[0]
        for ai in a:
            res &= ai
            for i in range(31):
                bfm[i] += (ai >> i) & 1
        for key, v in sorted(bfm.items(), key=lambda x: (-x[0], -x[1])):
            if k - (n - v) >= 0:
                k -= n - v
                res |= 1 << key
            if k == 0:
                break
        print(res)


if __name__ == "__main__":
    main()
