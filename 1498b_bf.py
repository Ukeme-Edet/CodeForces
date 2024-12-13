"""
@file: 1498b_bf.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Box Fitting(https://codeforces.com/problemset/problem/1498/B)
@version: 1.0
@date: 2024-12-13

@copyright: Copyright (c) 2024
"""

from collections import Counter
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        _, W = [int(x) for x in input().split()]
        wc = Counter([int(x) for x in input().split()])
        res = 0
        while any(wc.values()):
            res += 1
            cw = 0
            for k in sorted(wc.keys(), reverse=True):
                while wc[k] > 0 and cw + k <= W:
                    cw += k
                    wc[k] -= 1
        print(res)


if __name__ == "__main__":
    main()
