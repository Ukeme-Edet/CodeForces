from math import factorial
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, c = int(input()), 0
        a = sorted([int(x) for x in input().split()], key=lambda x: x % 2)
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if gcd(a[i], a[j] * 2) > 1:
                    c += 1
        print(c)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    main()
