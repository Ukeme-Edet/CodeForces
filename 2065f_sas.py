"""
@file: 2065f_sas.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Skibidus and Slay(https://codeforces.com/contest/2065/problem/F)
@version: 1.0
@date: 2025-03-19

@copyright: Copyright (c) 2025
"""

from collections import defaultdict
from sys import stdin, stdout
from typing import Counter


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        ch = [[] for _ in range(n + 1)]
        for i in range(n - 1):
            u, v = [int(x) for x in input().split()]
            ch[u].append(v)
            ch[v].append(u)
        res = ["0"] * n
        for i in range(1, n + 1):
            fm = defaultdict(int)
            for j in ch[i]:
                fm[str(a[j - 1])] += 1
            fm[str(a[i - 1])] += 1
            for k in fm.keys():
                if fm[k] > 1:
                    res[int(k) - 1] = "1"
        print("".join(res))


if __name__ == "__main__":
    main()
