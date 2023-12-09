from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, m = [int(_) for _ in input().split()]
        a = [[int(_) for _ in input().split()] for _ in range(n)]
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(ans, sumd(i, j, a))
        print(ans)


def sumd(i, j, a):
    return sumd_lr(i, j, a) + sumd_rl(i, j, a) - a[i][j]


def sumd_lr(i, j, a):
    k, l = i, j
    ans = 0
    while k > -1 and l > -1:
        ans += a[k][l]
        k -= 1
        l -= 1
    k, l = i, j
    while k < len(a) and l < len(a[0]):
        ans += a[k][l]
        k += 1
        l += 1
    return ans - a[i][j]


def sumd_rl(i, j, a):
    k, l = i, j
    ans = 0
    while k > -1 and l < len(a[0]):
        ans += a[k][l]
        k -= 1
        l += 1
    k, l = i, j
    while k < len(a) and l > -1:
        ans += a[k][l]
        k += 1
        l -= 1
    return ans - a[i][j]


if __name__ == "__main__":
    main()
