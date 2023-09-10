from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, a, b, c, d = [int(x) for x in input().split()]
        if (a - b) * n > c + d or (a + b) * n < c - d:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main()
