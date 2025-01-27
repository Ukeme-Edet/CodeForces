"""
@file: 1610b_ka.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Kalindrome Array(https://codeforces.com/contest/1610/problem/B)
@version: 1.0
@date: 2025-01-27

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    for _ in range(int(input())):
        n = int(input())
        a = [int(x) for x in input().split()]
        l, r = 0, n - 1
        while l < r:
            if a[l] == a[r]:
                l += 1
                r -= 1
            else:
                for x in [a[l], a[r]]:
                    l, r = 0, n - 1
                    while l < r:
                        if a[l] == x:
                            l += 1
                        elif a[r] == x:
                            r -= 1
                        elif a[l] == a[r]:
                            l += 1
                            r -= 1
                        else:
                            break
                    if l >= r:
                        break
                else:
                    break
        else:
            print("YES")
            continue
        print("NO")


if __name__ == "__main__":
    main()
