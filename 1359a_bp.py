from math import ceil
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, m, k = [int(x) for x in input().split()]
        cpp = n / k
        if max(m, cpp) == cpp:
            print(m)
            continue
        max2 = ceil((m - cpp) / (k - 1))
        print(int(cpp - max2))


if __name__ == "__main__":
    main()
