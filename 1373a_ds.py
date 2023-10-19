from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        a, b, c = [int(x) for x in input().split()]
        print(f"{1 if c > a else -1} {b if c / b < a else -1}")


if __name__ == "__main__":
    main()
