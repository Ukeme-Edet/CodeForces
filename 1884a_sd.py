from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        x, k = [int(x) for x in input().split()]
        while sum([int(x) for x in str(x)]) % k != 0:
            x += 1
        print(x)


if __name__ == "__main__":
    main()
