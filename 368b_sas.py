from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, m = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    dp, hash_map = [0] * n, [[] for i in range(100)]
    unique = 0
    for i in range(n - 1, -1, -1):
        hash_code = hash(a[i])
        if hash_map[hash_code]:
            if not a[i] in hash_map[hash_code]:
                unique += 1
                hash_map[hash_code].append(a[i])
        else:
            unique += 1
            hash_map[hash_code].append(a[i])
        dp[i] = unique
    for i in range(m):
        print(dp[int(input()) - 1])


def hash(n):
    return n % 100


if __name__ == "__main__":
    main()
