"""
@file: 1729d_fatr.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Friends and the Restaurant(https://codeforces.com/contest/1729/problem/D)
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
        x = [int(x) for x in input().split()]
        y = [int(x) for x in input().split()]
        diff = sorted(y[i] - x[i] for i in range(n))
        surp = diff[bisect_left(diff, 1) :]
        defi = diff[: bisect_left(diff, 0)][::-1]
        res = 0
        i = j = -1
        zc = diff.count(0)
        while -i <= len(defi) and -j <= len(surp):
            if surp[j] + defi[i] >= 0:
                res += 1
                j -= 1
            i -= 1
        print(res + (len(surp) + j + 1 + zc) // 2)


if __name__ == "__main__":
    main()
