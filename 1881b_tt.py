from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        ts = [int(x) for x in input().split()]
        ds = [x % min(ts) for x in ts]
        if sum(ds) > 0:
            print("NO")
            continue
        ts = [x // min(ts) - 1 for x in ts]
        if sum(ts) > 3:
            print("NO")
        else:
            print("YES")


if __name__ == "__main__":
    main()
