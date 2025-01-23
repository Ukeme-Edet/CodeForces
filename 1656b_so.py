"""
@file: 1656b_so.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Subtract Operation(https://codeforces.com/problemset/problem/1656/B)
@version: 1.0
@date: 2025-01-24

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        n, k = [int(_) for _ in input().split()]
        a = sorted(int(_) for _ in input().split())
        i, j = 0, 1
        while i < n and j < n:
            if a[j] - a[i] == k:
                print("YES")
                break
            elif a[j] - a[i] < k and j < n:
                j += 1
            else:
                i += 1
        else:
            print("NO")


if __name__ == "__main__":
    main()
