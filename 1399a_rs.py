from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = sorted([int(x) for x in input().split()])
        for i in range(n - 1):
            if a[i + 1] - a[i] > 1:
                print("NO")
                break
        else:
            print("YES")


if __name__ == "__main__":
    main()
