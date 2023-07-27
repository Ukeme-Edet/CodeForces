from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    res = n + (n * (n - 1) / 2)
    for i in range(n - 2):
        res += sum(n - 2 - i)
    print(int(res))


def sum(n):
    return n + (n * (n - 1) / 2)


if __name__ == "__main__":
    main()
