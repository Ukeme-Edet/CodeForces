"""
@file: 1765m_mlcm.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Minimum LCM(https://codeforces.com/problemset/problem/1765/M)
@version: 1.0
@date: 2024-10-29

@copyright: Copyright (c) 2024
"""

from math import gcd
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def seive(n):
    primes = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
    return [p for p in range(2, n + 1) if primes[p]]


def main():
    t = int(input())
    primes = seive(int((10**9) ** 0.5))
    for _ in range(t):
        n = int(input())
        for p in primes:
            if n % p == 0:
                a, b = n // p, n - n // p
                print(f"{a} {b}")
                break
        else:
            print(f"1 {n - 1}")


if __name__ == "__main__":
    main()
