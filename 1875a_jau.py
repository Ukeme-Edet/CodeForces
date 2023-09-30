from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        a, b, n = [int(x) for x in input().split()]
        x = [int(x) for x in input().split()]
        x = [a - 1 if x > a - 1 else x for x in x]
        print(sum(x) + b)


if __name__ == "__main__":
    main()