from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, m, k, h = map(int, input().split())
        hs = [int(x) for x in input().split()]
        c = 0
        for hss in hs:
            if abs(h - hss) % k == 0 and 0 < abs(h - hss) // k < m:
                c += 1
        print(c)


if __name__ == "__main__":
    main()
