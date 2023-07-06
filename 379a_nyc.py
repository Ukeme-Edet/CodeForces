from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    a, b = map(int, input().split())
    hours, next = 0, 0
    next = a
    while next >= 1:
        hours += next // 1
        next = ((next // 1) / b) + (next % 1)
    print(int(hours))


if __name__ == "__main__":
    main()
