"""
@file: 1904c_ag.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Array Game(https://codeforces.com/problemset/problem/1904/C)
@version: 1.0
@date: 2024-11-08

@copyright: Copyright (c) 2024
"""

from bisect import bisect_left
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


# def get_min(a, k):
#     if k == 0:
#         return min(a)
#     res = min(a)
#     for i in range(1, len(a)):
#         res = min(
#             res, min(get_min(a + [abs(a[i] - a[j])], k - 1) for j in range(i))
#         )
#     return res


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        a = sorted([int(x) for x in input().split()])
        if k > 2:
            print(0)
            continue
        a.sort()
        md = float("inf")
        if k == 2:
            mdiff = float("inf")
            for j in range(n):
                for i in range(j):
                    d = a[j] - a[i]
                    k = bisect_left(a, d)
                    diff = float("inf")
                    if k > 0:
                        diff = min(diff, d - a[k - 1])
                    if k < n:
                        diff = min(diff, a[k] - a[j] + a[i])
                    if diff < mdiff:
                        mdiff = diff
                        ta = d
                    md = min(md, d)
            a.append(ta if mdiff < md else md)
        a.sort()
        print(min(a[0], min(a[i] - a[i - 1] for i in range(1, n))))


if __name__ == "__main__":
    main()
