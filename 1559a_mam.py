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
        ans = min(a)
        for i in a:
            ans &= i
        print(ans)


if __name__ == "__main__":
    main()