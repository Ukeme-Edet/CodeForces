"""
@file: 1473e_cp.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Correct Placement(https://codeforces.com/problemset/problem/1473/E)
@version: 1.0
@date: 2025-04-09

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n = int(input())
        pp = [0] * n
        for i in range(n):
            pp[i] = sorted([int(x) for x in input().split()], reverse=True) + [
                i
            ]
        pp.sort(key=lambda x: x[:2])
        lm = float("inf")
        cm = pp[0][1]
        res = [-1] * n
        li = -1
        cli = pp[0][2]
        for i in range(1, n):
            if pp[i][0] > pp[i - 1][0]:
                if cm < lm:
                    li = cli
                    lm = cm
                cm = float("inf")
            if pp[i][1] < cm:
                cm = pp[i][1]
                cli = pp[i][2]
            if pp[i][1] > lm:
                res[pp[i][2]] = li + 1
        print(*res)


if __name__ == "__main__":
    main()
