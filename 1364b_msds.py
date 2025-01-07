"""
@file: 1364b_msds.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Most socially-distanced subsequence(https://codeforces.com/problemset/problem/1364/B)
@version: 1.0
@date: 2025-01-07

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
        p = [int(x) for x in input().split()]
        res = []
        for i in range(1, n - 1):
            if p[i - 1] < p[i] > p[i + 1] or p[i - 1] > p[i] < p[i + 1]:
                res.append(p[i])
        print(len(res) + 2)
        print(" ".join(str(x) for x in [p[0]] + res + [p[-1]]))


if __name__ == "__main__":
    main()
