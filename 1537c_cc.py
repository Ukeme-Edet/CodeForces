from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        h = sorted([int(_) for _ in input().split()])
        d = [0, 1]
        for i in range(n - 1):
            if h[i + 1] - h[i] < h[d[1]] - h[d[0]]:
                d = [i, i + 1]
        print(" ".join(str(_)
              for _ in [h[d[0]]] + h[d[1] + 1:] + h[:d[0]] + [h[d[1]]]))


if __name__ == "__main__":
    main()
