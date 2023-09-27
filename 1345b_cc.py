from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    build_h = {2: 1}
    ca = [2]
    for _ in range(t):
        n = int(input())
        np = 0
        if n < 2:
            print(0)
            continue
        while n > ca[-1]:
            h = build_h[ca[-1]] + 1
            c = ca[-1] + h * 2 + h - 1
            build_h[c] = h
            ca.append(c)
        while n > 1:
            i = binary_s(ca, n)
            n -= ca[i]
            np += 1
        print(np)


def binary_s(a, x):
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return r

if __name__ == "__main__":
    main()