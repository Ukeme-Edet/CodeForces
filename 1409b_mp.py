from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        a, b, x, y, n = [int(x) for x in input().split()]
        n = min(n, a - x + b - y)
        print(min(prod(a, x, b, n), prod(b, y, a, n)))


def prod(a, x, b, n):
    return max(x, a - n) * (b - n + (a - max(x, a - n)))


if __name__ == "__main__":
    main()
