"""
@file: 2065c2_saft.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Skibidus and Fanum Tax (hard version)(https://codeforces.com/contest/2065/problem/C2)
@version: 1.0
@date: 2025-03-19

@copyright: Copyright (c) 2025
"""

from bisect import bisect_left
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n, m = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        b = sorted([int(x) for x in input().split()])
        k = bisect_left(b, -float("inf"))
        a[0] = min(a[0], b[k] - a[0])
        for i in range(1, n):
            k = bisect_left(b, a[i] + a[i - 1])
            if k == m:
                continue
            mav, miv = max(b[k] - a[i], a[i]), min(b[k] - a[i], a[i])
            if miv >= a[i - 1]:
                a[i] = miv
            elif mav >= a[i - 1]:
                a[i] = mav
            else:
                print("NO")
                break
        else:
            print("YES" if a == sorted(a) else "NO")


if __name__ == "__main__":
    main()
