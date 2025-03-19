"""
@file: 2065e_sar.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Skibidus and Rizz(https://codeforces.com/contest/2065/problem/E)
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
        n, m, k = [int(x) for x in input().split()]
        if abs(n - m) > k or max(n, m) < k:
            print(-1)
            continue
        c = "01" if n > m else "10"
        n, m = sorted([n, m], reverse=True)
        print(
            c[0] * k
            + c[::-1] * min(m, n - k)
            + c[0] * (n - min(m, n - k) - k)
            + c[1] * (m - min(m, n - k))
        )


if __name__ == "__main__":
    main()
