from math import ceil
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        a, b, c = [int(x) for x in input().split()]
        diff = abs(a - b) / 2
        print(ceil(diff / c))


if __name__ == "__main__":
    main()
