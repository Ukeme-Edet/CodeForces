"""
@file: 2065c1_saft.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Skibidus and Fanum Tax (easy version)(https://codeforces.com/contest/2065/problem/C1)
@version: 1.0
@date: 2025-03-19

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n, m = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        b = int(input())
        a[0] = min(a[0], b - a[0])
        for i in range(1, n):
            mav, miv = max(b - a[i], a[i]), min(b - a[i], a[i])
            if miv >= a[i - 1]:
                a[i] = miv
            elif mav >= a[i - 1]:
                a[i] = mav
            else:
                print("NO")
                break
        else:
            print("YES")


if __name__ == "__main__":
    main()
