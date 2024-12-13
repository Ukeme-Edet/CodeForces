"""
@file: 1692e_bd.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Binary Deque(https://codeforces.com/problemset/problem/1692/E)
@version: 1.0
@date: 2024-12-12

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
        n, ts = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        tr = s = 0
        l = r = 0
        while r < n:
            s += a[r]
            while s > ts:
                s -= a[l]
                l += 1
            tr = max(tr, r - l + 1)
            r += 1
        print(n - tr if s == ts else -1)


if __name__ == "__main__":
    main()
