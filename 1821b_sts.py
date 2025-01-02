"""
@file: 1821b_sts.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Sort the Subarray(https://codeforces.com/problemset/problem/1821/B)
@version: 1.0
@date: 2025-01-02

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        ap = [int(x) for x in input().split()]
        l, r = 0, 1
        lr, rr = 0, 1
        while r < n:
            while r < n and ap[r - 1] <= ap[r]:
                r += 1
            lr, rr = (
                [l, r]
                if r - l >= rr - lr
                and not all(a[i] == ap[i] for i in range(l, r))
                else [lr, rr]
            )
            l = r
            r += 1
        print(f"{lr + 1} {rr}")


if __name__ == "__main__":
    main()
