"""
@file: 1167b_ln.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Lost Numbers(https://codeforces.com/problemset/problem/1167/B)
@version: 1.0
@date: 2025-04-09

@copyright: Copyright (c) 2025
"""

from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    ia = [4, 8, 15, 16, 23, 42]
    pm = {}
    for i in range(6):
        for j in range(6):
            if i == j:
                continue
            pm[ia[i] * ia[j]] = (ia[i], ia[j])
    print("? 1 2")
    stdout.flush()
    tr1 = pm[int(input())]
    print("? 1 3")
    stdout.flush()
    tr2 = pm[int(input())]
    a = [0] * 6
    if tr1[0] == tr2[0]:
        a[0] = tr1[0]
        a[1] = tr1[1]
        a[2] = tr2[1]
    elif tr1[0] == tr2[1]:
        a[0] = tr1[0]
        a[1] = tr1[1]
        a[2] = tr2[0]
    elif tr1[1] == tr2[0]:
        a[0] = tr1[1]
        a[1] = tr1[0]
        a[2] = tr2[1]
    else:
        a[0] = tr1[1]
        a[1] = tr1[0]
        a[2] = tr2[0]
    print("? 4 5")
    stdout.flush()
    tr1 = pm[int(input())]
    print("? 4 6")
    stdout.flush()
    tr2 = pm[int(input())]
    if tr1[0] == tr2[0]:
        a[3] = tr1[0]
        a[4] = tr1[1]
        a[5] = tr2[1]
    elif tr1[0] == tr2[1]:
        a[3] = tr1[0]
        a[4] = tr1[1]
        a[5] = tr2[0]
    elif tr1[1] == tr2[0]:
        a[3] = tr1[1]
        a[4] = tr1[0]
        a[5] = tr2[1]
    else:
        a[3] = tr1[1]
        a[4] = tr1[0]
        a[5] = tr2[0]
    print("! " + " ".join(str(x) for x in a))
    stdout.flush()


if __name__ == "__main__":
    main()
