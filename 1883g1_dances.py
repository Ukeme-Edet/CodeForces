"""
@file: 1883g1_dances.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Dances (Easy version)(https://codeforces.com/problemset/problem/1883/G1)
@version: 1.0
@date: 2024-11-09

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
        n, m = [int(x) for x in input().split()]
        a = [1] + sorted([int(x) for x in input().split()])
        b = sorted([int(x) for x in input().split()])
        i, j, k, l = 0, 0, n, n
        res = 0
        while i < k:
            if a[i] >= b[j]:
                res += 1
                j += 1
                k -= 1
            else:
                i += 1
                j += 1
        print(res)


if __name__ == "__main__":
    main()
