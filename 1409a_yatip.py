from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        a, b = [int(x) for x in input().split()]
        print((abs(a - b) + 9) // 10)


if __name__ == "__main__":
    main()
