from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        fs, fe = [int(x) for x in input().split()]
        printed = False
        for i in range(n - 1):
            s, e = [int(x) for x in input().split()]
            if printed:
                continue
            if s >= fs and e >= fe:
                print(-1)
                printed = True
        if not printed:
            print(fs)


if __name__ == "__main__":
    main()
