from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = input()
    print(n + "".join([x for x in reversed(n)]))


if __name__ == "__main__":
    main()
