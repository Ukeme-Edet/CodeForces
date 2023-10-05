from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, v, p = int(input()), 0, 0
    a = {0: 0 for _ in range(n)}
    {a.update({int(x) - 1: i}) for i, x in enumerate(input().split())}
    _ = int(input())
    b = [int(x) for x in input().split()]
    for i in b:
        v += a[i - 1] + 1
        p += n - a[i - 1]
    print(f"{v} {p}")


if __name__ == "__main__":
    main()
