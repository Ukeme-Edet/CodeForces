from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        count = 2
        while n % ((2 ** count) - 1) != 0:
            count += 1
        print(n // ((2 ** count) - 1))


if __name__ == "__main__":
    main()
