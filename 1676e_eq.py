from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, q = [int(x) for x in input().split()]
        a = sorted([int(x) for x in input().split()], reverse=True)
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + a[i - 1]
        for _ in range(q):
            x = int(input())
            l, r = 0, n
            while l < r:
                mid = (l + r) // 2
                if prefix[mid] >= x:
                    r = mid
                else:
                    l = mid + 1
            print(r if r - 1 < n and prefix[r] >= x else -1)


if __name__ == "__main__":
    main()
