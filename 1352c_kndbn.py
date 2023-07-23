from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        print(k + (k - 1) // (n - 1))


if __name__ == "__main__":
    main()
