"""
@file: 1691b_ss.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Shoe Shuffling(https://codeforces.com/problemset/problem/1691/B)
@version: 1.0
@date: 2025-02-02

@copyright: Copyright (c) 2025
"""

from collections import defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        n = int(input())
        s = input().split()
        sm = defaultdict(list)
        for i in range(n):
            sm[s[i]].append(i)
        if any(len(v) == 1 for v in sm.values()):
            print(-1)
            continue
        res = [0] * n
        for v in sm.values():
            for i in range(1, len(v)):
                res[v[i]] = v[i - 1] + 1
            res[v[0]] = v[-1] + 1
        print(" ".join(str(x) for x in res))


if __name__ == "__main__":
    main()
