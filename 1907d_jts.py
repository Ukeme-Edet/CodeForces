"""
@file: 1907d_jts.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Jumping Through Segments(https://codeforces.com/problemset/problem/1907/D)
@version: 1.0
@date: 2024-10-13

@copyright: Copyright (c) 2024
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def check(k, a):
    l, r = 0, 0
    for seg in a:
        l = max(l - k, seg[0])
        r = min(r + k, seg[1])
        if l > r:
            return False
    return True


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [[int(x) for x in input().split()] for _ in range(n)]
        res = float("inf")
        l, r = 0, 2000000000
        while l <= r:
            m = l + (r - l) // 2
            if check(m, a):
                res = m
                r = m - 1
            else:
                l = m + 1
        print(res)


if __name__ == "__main__":
    main()
