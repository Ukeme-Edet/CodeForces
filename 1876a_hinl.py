"""
@file: 1876a_hinl.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Helmets in Night Light(https://codeforces.com/problemset/problem/1876/A)
@version: 1.0
@date: 2024-10-08

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
        n, p = [int(_) for _ in input().split()]
        ab = [
            [int(x), int(y)] for x, y in zip(input().split(), input().split())
        ]
        ab.sort(key=lambda x: x[1])
        cost, nr, i = p, 1, 0
        while nr < n:
            if ab[i][1] < p:
                cost += min(n - nr, ab[i][0]) * ab[i][1]
                nr += min(n - nr, ab[i][0])
                i += 1
            else:
                cost += p * (n - nr)
                break
        print(cost)


if __name__ == "__main__":
    main()
