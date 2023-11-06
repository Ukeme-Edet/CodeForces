from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, k = [int(x) for x in input().split()]
    print(len([y for y in [int(x) for x in input().split()] if y <= 5 - k]) // 3)

if __name__ == "__main__":
    main()
