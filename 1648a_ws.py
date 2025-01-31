"""
@file: 1648a_ws.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Weird Sum(https://codeforces.com/problemset/problem/1648/A)
@version: 1.0
@date: 2025-01-31

@copyright: Copyright (c) 2025
"""

from collections import defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, m = [int(x) for x in input().split()]
    cm = defaultdict(lambda: defaultdict(list))
    for i in range(n):
        row = [x for x in input().split()]
        for j in range(m):
            cm[row[j]]["x"].append(j)
            cm[row[j]]["y"].append(i)
    res = 0
    for c in cm.values():
        c["x"].sort()
        for i in range(len(c["x"]) - 1):
            res += (
                (len(c["x"]) - i - 1)
                * (i + 1)
                * (c["x"][-i - 1] - c["x"][-i - 2])
            )
        c["y"].sort()
        for i in range(len(c["y"]) - 1):
            res += (
                (len(c["y"]) - i - 1)
                * (i + 1)
                * (c["y"][-i - 1] - c["y"][-i - 2])
            )
    print(res)


if __name__ == "__main__":
    main()
