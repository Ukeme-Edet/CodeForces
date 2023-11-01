from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        ms = 0
        psl, psr = [0] * n, [0] * n
        psld, psrd = {}, {}
        for i in range(1, n):
            if s[i - 1] not in psld:
                psld[s[i - 1]] = 0
                psl[i] = psl[i - 1] + 1
            else:
                psl[i] = psl[i - 1]
            if s[-i] not in psrd:
                psrd[s[-i]] = 0
                psr[-i - 1] = psr[-i] + 1
            else:
                psr[-i - 1] = psr[-i]
        for i in range(1, n):
            ms = max(ms, psl[i] + psr[i - 1])
        print(ms)


if __name__ == "__main__":
    main()
