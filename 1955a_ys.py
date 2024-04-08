from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, a, b = [int(x) for x in input().split()]
        if b / 2 >= a:
            print(n * a)
        else:
            print((n // 2) * b + (n % 2) * a)


if __name__ == "__main__":
    main()
