"""
@file: 1561c_ddb.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Deep Down Below(https://codeforces.com/problemset/problem/1561/C)
@version: 1.0
@date: 2024-12-12

@copyright: Copyright (c) 2024
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def fight(cvs, m):
    for cv in cvs:
        if all(m > x for x in cv):
            m += len(cv)
        else:
            return False
    return True


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        cvs = [[] for _ in range(n)]
        for i in range(n):
            cvs[i] = [int(x) - i + 1 for i, x in enumerate(input().split())][
                1:
            ]
        cvs.sort(key=lambda x: max(x))
        l, r = 0, 1000000002
        res = float("inf")
        while l < r:
            m = l + (r - l) // 2
            if fight(cvs, m):
                res = min(res, m)
                r = m
            else:
                l = m + 1
        print(res)


if __name__ == "__main__":
    main()
