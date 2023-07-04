from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, k = map(int, input().split())
    h = [int(x) for x in input().split()]
    dp = [None] * n
    dp[0] = sum(h[:k])
    smallest_i = 0
    for i in range(n-k):
        dp[i+1] = dp[i] - h[i] + h[i+k]
        if dp[i+1] < dp[smallest_i]:
            smallest_i = i+1
    print(smallest_i+1)


if __name__ == "__main__":
    main()
