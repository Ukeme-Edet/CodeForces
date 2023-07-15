from cmath import sqrt
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, x = map(int, input().split())
    factors = 0
    for i in range(1, int(sqrt(x).real) + 1):
        if x % i == 0 and x / i <= n:
            if x / i != i:
                factors += 2
            else:
                factors += 1
    print(factors)


if __name__ == "__main__":
    main()
