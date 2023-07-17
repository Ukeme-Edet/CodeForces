from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, a, b = map(int, input().split())
    print(n - a - max(0, n - a - b - 1))


if __name__ == "__main__":
    main()
