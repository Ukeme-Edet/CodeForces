"""
@file: 1615b_ainz.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem And It's Non-Zero(https://codeforces.com/contest/1615/problem/B)
@version: 1.0
@date: 2024-11-20

@copyright: Copyright (c) 2024
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    psb = [[0] * 200001 for _ in range(18)]
    for i in range(1, 200001):
        for j in range(18):
            psb[j][i] = psb[j][i - 1] + ((i >> j) & 1)
    for _ in range(t):
        l, r = [int(x) for x in input().split()]
        res = float("inf")
        for i in range(18):
            res = min(res, r - l + 1 - psb[i][r] + psb[i][l - 1])
        print(res)


if __name__ == "__main__":
    main()
