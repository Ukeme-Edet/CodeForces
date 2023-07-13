from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().split())
        a, b = map(int, input().split())
        if b > 2 * a:
            b = 2 * a
        print((min(x, y) * b) + (abs(x - y) * a))


if __name__ == "__main__":
    main()
