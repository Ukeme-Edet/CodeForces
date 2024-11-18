"""
@file: 1878e_iap.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Iva & Pav(https://codeforces.com/contest/1878/problem/E)
@version: 1.0
@date: 2024-11-18

@copyright: Copyright (c) 2024
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def find_max(l, r, bm):
    ans, ll = -1, l
    while l <= r:
        m = (l + r) >> 1
        if bm[m] - bm[ll - 1] == m - ll + 1:
            ans = max(ans, m)
            l = m + 1
        else:
            r = m - 1
    return ans


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        bps = [[0] * (n + 1) for _ in range(32)]
        for j in range(n):
            for i in range(32):
                bps[i][j + 1] = bps[i][j] + ((a[j] >> i) & 1)
        q = int(input())
        res = [0] * q
        for ii in range(q):
            l, k = [int(x) for x in input().split()]
            ans, i = -1, 31
            while i >= 0 and not (k >> i) & 1:
                ans = max(ans, find_max(l, n, bps[i]))
                i -= 1
            j = float("inf")
            while i >= 0:
                bs = find_max(l, n, bps[i])
                if (k >> i) & 1:
                    j = min(bs, j)
                else:
                    ans = max(ans, min(j, bs))
                i -= 1
            res[ii] = max(ans, j)
            if res[ii] < l:
                res[ii] = -1
        print(" ".join(str(x) for x in res))


if __name__ == "__main__":
    main()
