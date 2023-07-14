from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        if n % 2 != k % 2 or k ** 2 > n:
            print("NO")
        else:
            print("YES")


if __name__ == "__main__":
    main()
