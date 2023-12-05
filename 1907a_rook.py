from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    r = "abcdefgh"
    for _ in range(t):
        p = input()
        for i in range(1, 9):
            print(f"{p[0]}{i}") if int(p[1]) != i else ""
        for i in range(8):
            print(f"{r[i]}{p[1]}") if r[i] != p[0] else ""


if __name__ == "__main__":
    main()
