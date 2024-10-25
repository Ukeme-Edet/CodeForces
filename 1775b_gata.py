"""
@file: 1775b_gata.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Gardener and the Array(https://codeforces.com/problemset/problem/1775/B)
@version: 1.0
@date: 2024-10-25

@copyright: Copyright (c) 2024
"""

from collections import defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        bc = defaultdict(int)
        n = int(input())
        c = [[] for _ in range(n)]
        for i in range(n):
            p = [x for x in input().split()]
            for x in p[1:]:
                bc[x] += 1
            c[i] = p[1:]
        for i in range(n):
            if all(bc[x] > 1 for x in c[i]):
                print("Yes")
                break
        else:
            print("No")


if __name__ == "__main__":
    main()
