from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    m = n - input().count("1")
    print(n - min(m, n - m) * 2)


if __name__ == "__main__":
    main()
