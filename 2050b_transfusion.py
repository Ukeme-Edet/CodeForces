"""
@file: 2050b_transfusion.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Transfusion(https://codeforces.com/problemset/problem/2050/B)
@version: 1.0
@date: 2024-12-22

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
        a = [int(x) for x in input().split()]
        os = sum(a[i] for i in range(0, n, 2))
        es = sum(a[i] for i in range(1, n, 2))
        print(
            "YES"
            if not es % (n // 2)
            and not os % ((n + 1) // 2)
            and es // (n // 2) == os // ((n + 1) // 2)
            else "NO"
        )


if __name__ == "__main__":
    main()
