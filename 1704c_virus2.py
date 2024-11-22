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
    

def testcase():
    n, m = [int(x) for x in input().split()]
    a = sorted([int(x) for x in input().split()])
    saveable = [n - a[-1] + a[0] - 1]
    for i in range(m - 1):
        saveable.append(a[i + 1] - a[i] - 1)
    saveable.sort(reverse=True)
    saved = 0
    r = 1
    for inter in saveable:
        if inter - r <= 0:
            saved += 1 if (inter - r == 0) else 0
            break
        saved += inter - r
        r += 4
    print(n - saved)


def main():
    t = int(input())
    for _ in range(t):
    	testcase()


if __name__ == "__main__":
    main()
