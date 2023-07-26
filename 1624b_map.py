from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        na = b * 2 - c
        if na % a == 0 and na >= a:
            print("YES")
            continue
        nb = a + ((c - a) / 2)
        if nb % b == 0 and nb >= b:
            print("YES")
            continue
        nc = 2 * b - a
        if nc % c == 0 and nc >= c:
            print("YES")
            continue
        print("NO")


if __name__ == "__main__":
    main()
