from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        i = 0
        while i < n and a[i] == 1:
            i += 1
        print("First" if ((i % 2 == 0 and sum(a) != n) or (
            sum(a) == n and i % 2 == 1)) else "Second")


if __name__ == "__main__":
    main()
