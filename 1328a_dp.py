from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        print(0 if a % b == 0 else b - a % b)


if __name__ == "__main__":
    main()
