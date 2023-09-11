from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        print(k - n if k > n else abs((k % 2) - (n % 2)))


if __name__ == "__main__":
    main()
