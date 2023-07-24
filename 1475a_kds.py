from math import ceil
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        cf = (n + k - 1) // k
        print(((cf * k) + n - 1) // n)


if __name__ == "__main__":
    main()
