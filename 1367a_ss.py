from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        print(s[0] + "".join([s[i] for i in range(1, len(s) - 1, 2)]) + s[-1])


if __name__ == "__main__":
    main()
