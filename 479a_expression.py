from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    a, b, c = int(input()), int(input()), int(input())
    print(max(a + b + c, a * b * c, (a + b) *
          c, a * (b + c), a + b * c, a * b + c))


if __name__ == "__main__":
    main()
