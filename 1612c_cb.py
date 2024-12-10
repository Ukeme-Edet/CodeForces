"""
@file: 1612c_cb.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Chat Ban(https://codeforces.com/problemset/problem/1612/C)
@version: 1.0
@date: 2024-12-10

@copyright: Copyright (c) 2024
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def emotes_sent(m, k):
    if m > k:
        return k * (k + 1) // 2 + (m - k) * (3 * k - m - 1) // 2
    return m * (m + 1) // 2


def main():
    t = int(input())
    for _ in range(t):
        k, x = [int(x) for x in input().split()]
        l, r = 1, k * 2 - 1
        while l < r:
            m = l + (r - l) // 2
            es = emotes_sent(m, k)
            if es < x:
                l = m + 1
            else:
                r = m
        print(l)


if __name__ == "__main__":
    main()
