"""
@file: 1832b_ms.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Maximum Sum(https://codeforces.com/problemset/problem/1832/B)
@version: 1.0
@date: 2024-11-17

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
        n, k = [int(x) for x in input().split()]
        a = sorted(int(x) for x in input().split())
        pas = [0] * (n + 1)
        for i in range(n):
            pas[i + 1] = pas[i] + a[i]
        res = 0
        for i in range(k + 1):
            res = max(
                res, pas[-1] - (pas[i * 2] + pas[-1] - pas[-(k - i) - 1])
            )
        print(res)


if __name__ == "__main__":
    main()
