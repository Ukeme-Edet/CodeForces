from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    c = sum([int(x) for x in input().split()])
    print(c // 5 if c % 5 == 0 and c != 0 else -1)


if __name__ == "__main__":
    main()
