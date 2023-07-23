from cmath import sqrt
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, c = [int(x) for x in input().split()]
        s = [int(x) for x in input().split()]
        a, b, d = n, 2 * sum(s), sum([x ** 2 for x in s]) - c
        x1, x2 = (-b + sqrt((b ** 2) - (4 * a * d))) / \
            (2 * a), (-b - sqrt((b ** 2) - (4 * a * d))) / (2 * a)
        print(int(x1.real // 2) if x1.real % 1 == 0 else int(x2.real // 2))


if __name__ == "__main__":
    main()
