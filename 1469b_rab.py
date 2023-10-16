from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        r = [int(x) for x in input().split()]
        m = int(input())
        b = [int(x) for x in input().split()]
        dp = [[-1e9 for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0][0] = 0
        ans = 0
        for i in range(n + 1):
            for j in range(m + 1):
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + r[i - 1])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1] + b[j - 1])
                ans = max(ans, dp[i][j])
        print(ans)


if __name__ == "__main__":
    main()
