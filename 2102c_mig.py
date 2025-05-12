"""
@file: 2102c_mig.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Mex in the Grid(https://codeforces.com/contest/2102/problem/C)
@version: 1.0
@date: 2025-05-12

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n = int(input())
        res = [[0] * n for _ in range(n)]
        mx, my = 1, 0
        xm = ym = 0
        mxm = mym = 1
        xd = yd = -1
        x = y = n // 2
        for i in range(n * n):
            res[x][y] = i
            if mx:
                x += xd
                xm += 1
            else:
                y += yd
                ym += 1
            if xm == mxm:
                xm = 0
                mxm += 1
                mx = 0
                xd *= -1
            if ym == mym:
                ym = 0
                mym += 1
                mx = 1
                yd *= -1
        print("\n".join(" ".join(str(x) for x in row) for row in res))


if __name__ == "__main__":
    main()
