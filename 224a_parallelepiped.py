from math import sqrt
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    x, y, z = [int(x) for x in input().split()]
    a, b, c = sqrt(x * y / z), sqrt(z * x / y), sqrt(y * z / x)
    print(int(4 * (a + b + c)))


if __name__ == "__main__":
    main()
