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
        dp, max_s = [0] * n, 0
        for i in range(n):
            if not dp[i]:
                stack, j = [], i
                while j < n and not dp[j]:
                    stack.append((a[j], j))
                    j += a[j]
                if j >= n:
                    ai, j = stack.pop()
                    dp[j] = a[j]
                while stack:
                    ai, j = stack.pop()
                    dp[j] = dp[j + a[j]] + ai
                max_s = max(max_s, dp[i])
        print(max_s)


if __name__ == "__main__":
    main()
