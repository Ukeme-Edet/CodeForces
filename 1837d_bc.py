"""
@file: 1837d_bc.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Bracket Coloring(https://codeforces.com/problemset/problem/1837/D)
@version: 1.0
@date: 2024-11-20

@copyright: Copyright (c) 2024
"""

from collections import Counter
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        fm = Counter(s)
        if fm["("] != fm[")"]:
            print(-1)
            continue
        i = ob = 0
        res = [0] * n
        while i < n:
            ob += 1 if s[i] == "(" else -1
            if ob == 0 and s[i] == ")" or ob > 0:
                res[i] = 1
            else:
                res[i] = 2
            i += 1
        d = set(res)
        print(len(d))
        if len(d) == 1 and res[0] == 2:
            res = [1] * n
        print(" ".join(str(x) for x in res))


if __name__ == "__main__":
    main()
