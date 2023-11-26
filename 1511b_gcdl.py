from operator import indexOf
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        a, b, c = [int(_) for _ in input().split()]
        print("1" + "0" * (a - 1) + " " + "1" * (b - c + 1) + "0" * (c - 1))


if __name__ == "__main__":
    main()
