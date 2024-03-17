from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arrs = [[] for _ in range(n)]
        for i in range(n):
            _ = input()
            arrs[i] = sorted(int(x) for x in input().split())
        arrs.sort(key=lambda x: x[1])
        ans = 0
        mf = 10**9
        for i in range(1, n):
            mf = min(mf, arrs[i][0])
            ans += arrs[i][1]
        mf = min(mf, arrs[0][0])
        ans += mf
        print(ans)


if __name__ == "__main__":
    main()
