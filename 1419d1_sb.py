from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    a = sorted([int(_) for _ in input().split()])
    print(n // 2 if n % 2 else n // 2 - 1)
    for i in range(n // 2):
        stdout.write(f"{a[n // 2 + i]} {a[i]} ")
    print(a[-1] if n % 2 else "")


if __name__ == "__main__":
    main()
