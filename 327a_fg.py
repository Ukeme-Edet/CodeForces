from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    s, l, r = ''.join(input().split()), 0, n - 1
    ans = 0
    for i in range(n):
        for j in range(i, n):
            ans = max(ans, s[:i].count('1') +
                      s[i:j + 1].count('0') + s[j + 1:].count('1'))
    print(ans)


if __name__ == "__main__":
    main()
