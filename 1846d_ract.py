from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, d, h = map(int, input().split())
        y = [int(x) for x in input().split()]
        tri_a, area = d * h / 2, 0
        for i in range(n):
            area += tri_a
            if i < n - 1 and y[i + 1] - y[i] < h:
                x = d * (h - y[i + 1] + y[i]) / h
                yh = h - y[i + 1] + y[i]
                area -= yh * x / 2
        print(area)


if __name__ == "__main__":
    main()
