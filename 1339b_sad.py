from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string))


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = sorted([int(_) for _ in input().split()])
        c = n // 2
        for i in range(n // 2):
            print(f"{a[c + i]} {a[c - i - 1]} ")
        if n % 2:
            print(f"{a[-1]}")
        print("\n")


if __name__ == "__main__":
    main()
