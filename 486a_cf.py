from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    x = int(input())
    print(x // 2 if x % 2 == 0 else x//2-x)


if __name__ == "__main__":
    main()
