from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    a = input()
    print(a[:a.index("0")] + a[a.index("0") + 1:] if "0" in a else a[:-1])


if __name__ == "__main__":
    main()
