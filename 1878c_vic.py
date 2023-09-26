from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k, x = [int(x) for x in input().split()]
        if (k * (k + 1) // 2) <= x and x <= (k * (2 * n - k + 1) // 2):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
