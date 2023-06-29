from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    print(4 - len(set(input().split())))


if __name__ == "__main__":
    main()
