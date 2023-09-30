from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    if n % 2 == 0:
        print(2 ** (n // 2))
    else:
        print(0)


if __name__ == "__main__":
    main()
