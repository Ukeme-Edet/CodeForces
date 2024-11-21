"""
@file: 1143c_queen.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Queen(https://codeforces.com/contest/1143/problem/C)
@version: 1.0
@date: 2024-11-21

@copyright: Copyright (c) 2024
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    rc, p, cc = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
    for i in range(1, n + 1):
        pi, ci = [int(x) for x in input().split()]
        if pi == -1:
            continue
        rc[pi] += ci
        p[i] = ci
        cc[pi] += 1
    res = []
    for i in range(1, n + 1):
        if rc[i] == cc[i] and p[i]:
            res.append(i)
    print(" ".join(str(x) for x in res) if res else -1)


if __name__ == "__main__":
    main()
