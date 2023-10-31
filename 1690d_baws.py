from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        s = input()
        l, r = 0, k
        res = wc = s.count("W", l, r)
        while r < n:
            if s[r] == "W":
                wc += 1
            if s[l] == "W":
                wc -= 1
            res = min(res, wc)
            l += 1
            r += 1
        print(res)


if __name__ == "__main__":
    main()
