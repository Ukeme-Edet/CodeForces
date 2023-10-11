from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [int(x) - i for i, x in enumerate(input().split())]
        resm = {}
        res = 0
        for ai in a:
            if ai in resm:
                res += resm[ai]
            else:
                resm[ai] = 0
            resm[ai] += 1
        print(res)


if __name__ == "__main__":
    main()
