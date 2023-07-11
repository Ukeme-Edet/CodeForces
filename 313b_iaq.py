from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    s = input()
    dp = [0] * len(s)
    sum = 0
    for i in range(len(s) - 2, -1, -1):
        if s[i + 1] == s[i]:
            sum += 1
        dp[i] = sum
    m = int(input())
    for _ in range(m):
        l, r = map(int, input().split())
        print(dp[l - 1] - dp[r - 1])


if __name__ == "__main__":
    main()
