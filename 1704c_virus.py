"""
@file: 1704c_virus.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Virus(https://codeforces.com/problemset/problem/1704/C)
@version: 1.0
@date: 2024-11-22

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
        n, m = [int(x) for x in input().split()]
        a = sorted(int(x) for x in input().split())
        savable = sorted(
            [a[i] - a[i - 1] - 1 for i in range(1, m)]
            + [n - a[-1] + a[0] - 1],
            reverse=True,
        )
        dp = res = 0
        for save in savable:
            if save > dp * 2:
                res += 1
                dp += 2
                if save > (dp - 1) * 2:
                    res += save - (dp - 1) * 2
            else:
                break
        print(n - res)


if __name__ == "__main__":
    main()
