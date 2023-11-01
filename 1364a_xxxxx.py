from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, x = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        asum = sum(a)
        if asum % x:
            print(n)
            continue
        i = 0
        ans = -1
        while i < n:
            if a[i] % x:
                break
            i += 1
        if n - i:
            ans = n - i - 1
        else:
            print(-1)
            continue
        i = n
        while i > -1:
            i -= 1
            if a[i] % x:
                break
        print(max(ans, i))


if __name__ == "__main__":
    main()
