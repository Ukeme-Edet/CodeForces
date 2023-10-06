from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    a = input()
    b = input()
    print(-1 if a == b else max(len(a), len(b)))


if __name__ == "__main__":
    main()
