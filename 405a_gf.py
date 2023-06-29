from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    _ = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print(" ".join(map(str, a)))


if __name__ == "__main__":
    main()
