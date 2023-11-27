from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = [int(_) for _ in input()]
    i = 0
    while len(n) > 1:
        n = sum(n)
        n = [int(_) for _ in str(n)]
        i += 1
    print(i)


if __name__ == "__main__":
    main()
