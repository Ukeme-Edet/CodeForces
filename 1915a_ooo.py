from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        a, b, c = [int(_) for _ in input().split()]
        print(a if b == c else b if a == c else c)


if __name__ == "__main__":
    main()
