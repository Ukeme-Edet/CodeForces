from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        w = [int(_) for _ in input().split()]
        pr, pl = [w[-1]] * n, [w[0]] * n
        for i in range(1, n):
            pl[i] = pl[i - 1] + w[i]
            pr[i] = pr[i - 1] + w[n - i - 1]
        ans = 0
        for i in range(n):
            tans = binary_search(pl, pr[i])
            if i + 2 <= n - tans and tans > -1:
                ans = max(ans, tans + i + 2)
        print(ans)


def binary_search(arr, ele):
    l, r = 0, len(arr)
    while l < r:
        i = (l + r) // 2
        if arr[i] == ele:
            return i
        elif arr[i] < ele:
            l = i + 1
        else:
            r = i
    return i if arr[i] == ele else -1


if __name__ == "__main__":
    main()
