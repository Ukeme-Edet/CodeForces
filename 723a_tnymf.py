from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    x = [int(x) for x in input().split()]
    print(max(x) - min(x))


if __name__ == "__main__":
    main()
