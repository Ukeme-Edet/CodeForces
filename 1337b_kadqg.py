from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        x, n, m = map(int, input().split())
        while n > 0 and x > 20:
            x = (x // 2) + 10
            n -= 1
        while m > 0 and x > 0:
            x -= 10
            m -= 1
        print("YES" if x < 1 else "NO")


if __name__ == "__main__":
    main()
