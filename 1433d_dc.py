"""
@file: 1433d_dc.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Districts Connection(https://codeforces.com/problemset/problem/1433/D)
@version: 1.0
@date: 2025-01-22

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        n = int(input())
        a = sorted((int(i), idx) for idx, i in enumerate(input().split()))
        if a[0][0] == a[-1][0]:
            print("NO")
        else:
            print("YES")
            res = []
            for i in range(1, n):
                if a[i][0] != a[0][0]:
                    res.append((a[0][1] + 1, a[i][1] + 1))
            for i in range(1, n):
                if a[i][0] == a[0][0]:
                    res.append((a[i][1] + 1, a[-1][1] + 1))
            print("\n".join(f"{i} {j}" for i, j in res))


if __name__ == "__main__":
    main()
