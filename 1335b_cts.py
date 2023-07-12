from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for _ in range(t):
        n, a, b = [int(x) for x in input().split()]
        print(alpha[:b] * (n // b) + alpha[:n % b])


if __name__ == "__main__":
    main()
