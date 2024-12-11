"""
@file: 762a_kthd.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem k-th divisor(https://codeforces.com/problemset/problem/762/A)
@version: 1.0
@date: 2024-12-11

@copyright: Copyright (c) 2024
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, k = [int(x) for x in input().split()]
    facs = []
    for i in range(1, int(n**0.5) + 1):
        if not n % i:
            facs.append(i)
            if i != n // i:
                facs.append(n // i)
    print(-1 if len(facs) < k else sorted(facs)[k - 1])


if __name__ == "__main__":
    main()
