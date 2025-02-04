"""
@file: 1520e_ats.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Arranging The Sheep(https://codeforces.com/contest/1520/problem/E)
@version: 1.0
@date: 2025-02-04

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep="", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n = int(input())
        s = input()
        cs = [i + 1 for i in range(n) if s[i] == "*"]
        ps = [0] * (len(cs) + 1)
        for i in range(len(cs)):
            ps[i + 1] = ps[i] + cs[i]
        res = float("inf")
        for i in range(len(cs)):
            res = min(
                res,
                (i * cs[i] - ps[i] - i * (i + 1) // 2)
                + (ps[-1] - ps[i + 1] - (len(cs) - i - 1) * cs[i])
                - (len(cs) - i - 1) * (len(cs) - i) // 2,
            )
        print(res if res != float("inf") else 0)


if __name__ == "__main__":
    main()
