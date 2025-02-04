"""
@file: 1447b_nb.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Numbers Box(https://codeforces.com/problemset/problem/1447/B)
@version: 1.0
@date: 2024-09-01

@copyright: Copyright (c) 2024
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, m = [int(_) for _ in input().split()]
        a, nc = [], 0
        for _ in range(n):
            a.extend([int(_) for _ in input().split()])
        for i in range(n * m):
            if a[i] < 0:
                nc += 1
        a = sorted([abs(i) for i in a])
        if 0 in a or not nc % 2:
            print(sum(a))
        else:
            print(sum(a) - 2 * a[0])


if __name__ == "__main__":
    main()
