from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        a, b = [int(x) for x in input().split()]
        print(min(a, b, (a + b) // 3))


if __name__ == "__main__":
    main()
