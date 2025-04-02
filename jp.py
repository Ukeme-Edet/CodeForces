"""
@file: jp.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Jeopardized Projects(https://codeforces.com/gym/103886/problem/E)
@version: 1.0
@date: 2025-04-02

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


MOD = 10**9 + 7


def main():
    cn, cp = 1, 1
    ps = [0] * (10**5 + 1)
    for i in range(10**5):
        ps[i + 1] = ps[i] + cn - cp
        cn *= 2
        cn %= MOD
        if not i % 2:
            cp *= 2
            cp %= MOD
    for _ in range(int(input())):
        l, r = [int(x) for x in input().split()]
        print((ps[r] - ps[l - 1]) % MOD)


if __name__ == "__main__":
    main()
