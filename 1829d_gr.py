from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, m = [int(_) for _ in input().split()]
        print("YES" if find_pile(n, m, {}) else "NO")


def find_pile(n, m, dp={}):
    if n in dp:
        return dp[n]
    if n == m:
        return True
    if n < m:
        dp[n] = False
        return dp[n]
    if not n % 3:
        if n // 3 not in dp:
            dp[n // 3] = find_pile(n // 3, m, dp)
        if (n // 3) * 2 not in dp:
            dp[(n // 3) * 2] = find_pile((n // 3) * 2, m, dp)
        return dp[n // 3] or dp[(n // 3) * 2]
    dp[n] = False
    return dp[n]


if __name__ == "__main__":
    main()
