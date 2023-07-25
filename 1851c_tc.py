from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        c = [int(x) for x in input().split()]
        kc, en, st = 0, c[n - 1], c[0]
        for i in range(n - 1, -1, -1):
            if c[i] == en:
                kc += 1
            if kc == k:
                break
        c = c[:i]
        if ((c and c.count(c[0]) >= k) or en == st) and kc == k:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
