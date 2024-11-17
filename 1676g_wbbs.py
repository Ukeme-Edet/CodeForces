"""
@file: 1676g_wbbs.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem White-Black Balanced Subtrees(https://codeforces.com/contest/1676/problem/G)
@version: 1.0
@date: 2024-11-17

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
        n = int(input())
        a = [int(x) for x in input().split()]
        s = input()
        cc = [(0, 0)] * (n + 1)
        for i in range(n - 2, -1, -1):
            cc[i + 2] = (
                cc[i + 2][0] + (s[i + 1] == "W"),
                cc[i + 2][1] + (s[i + 1] == "B"),
            )
            cc[a[i]] = (cc[a[i]][0] + cc[i + 2][0], cc[a[i]][1] + cc[i + 2][1])
        cc[1] = (cc[1][0] + (s[0] == "W"), cc[1][1] + (s[0] == "B"))
        res = 0
        for i in range(1, n + 1):
            res += cc[i][0] == cc[i][1]
        print(res)


if __name__ == "__main__":
    main()
