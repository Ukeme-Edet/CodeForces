from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(n // 2 if n % 2 == 1 else n // 2 - 1)


if __name__ == "__main__":
    main()
