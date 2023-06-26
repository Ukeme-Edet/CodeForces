from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    p = list(map(int, input().split()))
    print(sum(p) / n)


if __name__ == "__main__":
    main()
