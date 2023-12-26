from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = sorted([(int(x), i)
                   for i, x in enumerate(input().split())], key=lambda x: x[0])
        to = 0
        for i in range(n):
            for j in range(i + 1, n):
                prod = a[i][0] * a[j][0]
                if prod > 2 * n:
                    break
                if prod == a[i][1] + a[j][1] + 2:
                    to += 1
        print(to)


if __name__ == "__main__":
    main()
