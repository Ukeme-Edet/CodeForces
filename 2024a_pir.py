"""
@file: 2024a_pir.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Profitable Interest Rate(https://codeforces.com/contest/2024/problem/A)
@version: 1.0
@date: 2024-10-20

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
        a, b = [int(x) for x in input().split()]
        x = float("inf")
        l, r = 0, 10**9
        while l <= r:
            mid = (l + r) // 2
            if b - a <= mid:
                x = min(x, mid)
                r = mid - 1
            else:
                l = mid + 1
        print(max(0, a - x))


if __name__ == "__main__":
    main()
