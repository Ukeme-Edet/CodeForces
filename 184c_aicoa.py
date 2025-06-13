"""
@file: 184c_aicoa.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem An impassioned circulation of affection(https://codeforces.com/problemset/problem/814/C)
@version: 1.0
@date: 2025-06-13

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    n = int(input())
    s = input()
    q = int(input())
    dp = [[0] * 26 for _ in range(n + 1)]
    for c in "".join(chr(i) for i in range(ord("a"), ord("z") + 1)):
        for i in range(1, n + 1):
            l = r = res = cc = 0
            while r < n:
                cc += s[r] == c
                if r - l + 1 - cc <= i:
                    res = max(res, r - l + 1)
                    r += 1
                else:
                    cc -= s[l] == c
                    l += 1
            dp[i][ord(c) - ord("a")] = res
    for _ in range(q):
        m, c = input().split()
        m = int(m)
        print(dp[m][ord(c) - ord("a")])


if __name__ == "__main__":
    main()
