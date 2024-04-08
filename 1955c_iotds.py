from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        l, r = 0, n - 1
        tu = 0
        while l <= r and k > 0:
            dt = min(k // 2 + k % 2, a[l], a[r])
            a[l] -= dt
            a[r] -= dt if l != r else 0
            k -= 2 * dt if l != r else dt
            if k < 0:
                a[r] += 1
            if a[l] == 0:
                l += 1
            if a[r] == 0:
                r -= 1
        print(a.count(0))


if __name__ == "__main__":
    main()
