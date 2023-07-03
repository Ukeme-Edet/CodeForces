from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, m = map(int, input().split())
    if min(n, m) % 2 == 0:
        print("Malvika")
    else:
        print("Akshat")


if __name__ == "__main__":
    main()
