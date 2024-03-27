from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, q = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        ps = [0] * (n + 1)
        for i in range(1, n + 1):
            ps[i] = ps[i - 1] + a[i - 1]
        for _ in range(q):
            l, r, k = [int(x) for x in input().split()]
            if (ps[l - 1] + ps[n] - ps[r] + k * (r - l + 1)) % 2:
                print("YES")
            else:
                print("NO")


if __name__ == "__main__":
    main()
