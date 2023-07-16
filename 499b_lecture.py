from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, m = map(int, input().split())
    wdict = {}
    for _ in range(m):
        w1, w2 = input().split()
        wdict[w1] = w2
    print(" ".join([wdict[w] if len(wdict[w]) <
          len(w) else w for w in input().split()]))


if __name__ == "__main__":
    main()
