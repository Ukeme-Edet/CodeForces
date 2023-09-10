from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    a = sorted([int(x) for x in input().split()], reverse=True)
    for i in range(n - 2):
        if a[i] < a[i + 1] + a[i + 2]:
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    main()
