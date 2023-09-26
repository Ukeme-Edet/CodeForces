from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        if k in a:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
