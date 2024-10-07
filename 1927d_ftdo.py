"""
@file: 1927d_ftdo.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Find the Different Ones!(https://codeforces.com/problemset/problem/1927/D)
@version: 1.0
@date: 2024-10-07

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
        n = int(input())
        a = [int(_) for _ in input().split()]
        psa = [-1] * n
        for i in range(1, n):
            psa[i] = i - 1 if a[i] != a[i - 1] else psa[i - 1]
        q = int(input())
        for _ in range(q):
            l, r = [int(_) for _ in input().split()]
            l -= 1
            r -= 1
            print(
                f"{psa[r] + 1} {r + 1}"
                if psa[r] >= l and psa[r] != psa[l]
                else "-1 -1"
            )


if __name__ == "__main__":
    main()
