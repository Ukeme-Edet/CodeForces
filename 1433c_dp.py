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
        dom, i = -2, 0
        while i < n - 1 and a[i] == a[i + 1]:
            i += 1
        if i == n - 1:
            print(-1)
            continue
        if a[i] < a[i + 1]:
            dom = i + 1
        else:
            dom = i
        i = dom + 1
        a[dom] += dom
        while i < n:
            if a[dom] <= a[i]:
                dom = i
            a[dom] += 1
            i += 1
        print(dom + 1 if a[dom] != a[abs(dom - 1)] else -1)


if __name__ == "__main__":
    main()
