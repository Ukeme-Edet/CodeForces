from math import inf
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        d = [[] for _ in range(201)]
        for i in range(n):
            di, si = [int(x) for x in input().split()]
            d[di].append(si)
            d[di].sort()
        maxr = inf
        for i in range(201):
            if d[i]:
                maxr = min(maxr, i + d[i][0] // 2 - (1 - d[i][0] % 2))
            if i > maxr:
                break
        print(maxr)


if __name__ == "__main__":
    main()
