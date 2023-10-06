from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    m = int(input())
    q = [int(x) for x in input().split()]
    s = [1] * n
    e = [a[0]] * n
    for i in range(1, n):
        s[i] = s[i - 1] + a[i - 1]
        e[i] = e[i - 1] + a[i]
    for qry in q:
        l, r = 0, n
        while l < r:
            m = (l + r) // 2
            if s[m] <= qry and e[m] >= qry:
                print(m + 1)
                break
            elif s[m] > qry:
                r = m
            else:
                l = m + 1


if __name__ == "__main__":
    main()
