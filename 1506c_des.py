from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        a, b = input(), input()
        if len(a) > len(b):
            a, b = b, a
        ans = 0
        for i in range(len(a)):
            for j in range(i + 1, len(a) + 1):
                if a[i:j] in b:
                    ans = max(ans, j - i)
        print(len(a) + len(b) - 2 * ans)


if __name__ == "__main__":
    main()
