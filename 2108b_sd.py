"""
@file: 2108b_sd.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem SUMdamental Decomposition(https://codeforces.com/contest/2108/problem/B)
@version: 1.0
@date: 2025-05-02

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n, x = [int(x) for x in input().split()]
        rn = max(0, n - x.bit_count())
        bpc = {i: x & (1 << i) for i in range(32)}
        i = 0
        res = x
        while rn and i < 32:
            if n - bpc[i] > 1:
                res += (1 << i) * min((rn + 1) // 2, (n - bpc[i]) // 2) * 2
                rn -= min(rn, (n - bpc[i]) // 2 * 2)
            i += 1
        if rn:
            print(-1)
            continue
        print(res)


if __name__ == "__main__":
    main()
