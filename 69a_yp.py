from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    x, y, z = [], [], []
    for _ in range(n):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        z.append(c)
    if sum(x) == 0 and sum(y) == 0 and sum(z) == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
