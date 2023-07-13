from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    _ = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(sum(a) - sum(b))
    print(sum(b) - sum([int(x) for x in input().split()]))


if __name__ == "__main__":
    main()
