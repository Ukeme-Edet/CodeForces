"""
@file: 1599c_br.py
@author: Ukeme Edet (ukemeedet2207@gmail.com)
@brief: The solution to the problem Berland Regional(https://codeforces.com/problemset/problem/1599/C)
@version: 1.0
@date: 2025-02-05

@copyright: Copyright (c) 2025
"""

from collections import defaultdict, deque
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(*args, sep=" ", end="\n"):
    return stdout.write(sep.join(str(x) for x in args) + end)


def main():
    for _ in range(int(input())):
        n = int(input())
        u = input().split()
        s = [int(x) for x in input().split()]
        ul = defaultdict(list)
        for i in range(n):
            ul[u[i]].append(s[i])
        ts = sorted(
            [sorted(x, reverse=True) for x in ul.values()],
            key=lambda x: len(x),
        )
        ma = sum(sum(x) for x in ts)
        tq = deque(ts)
        qps = deque()
        for i in range(len(tq)):
            ps = [0] * (len(tq[i]) + 1)
            for j in range(len(tq[i])):
                ps[j + 1] = ps[j] + tq[i][j]
            qps.append(ps)
        ans = [0] * n
        for i in range(n):
            while tq and len(tq[0]) <= i:
                ma -= sum(tq.popleft())
                qps.popleft()
            ta = ma
            for j in range(len(tq)):
                r = len(tq[j]) % (i + 1)
                ta -= qps[j][-1] - qps[j][-r - 1]
            ans[i] = ta
        print(*ans)


if __name__ == "__main__":
    main()
