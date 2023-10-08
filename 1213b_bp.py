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
        bad, mp = 0, a[-1]
        for i in range(n - 1, -1, -1):
            mp = min(mp, a[i])
            if a[i] > mp:
                bad += 1
        print(bad)


if __name__ == "__main__":
    main()
