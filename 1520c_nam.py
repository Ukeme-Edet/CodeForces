from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n == 1:
            print(n)
            continue
        if n == 2:
            print(-1)
            continue
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        j = 0
        for i in range(1, n * n + 1, 2):
            matrix[j // n][j % n] = i
            j += 1
        for i in range(2, n * n + 1, 2):
            matrix[j // n][j % n] = i
            j += 1
        for i in range(n):
            print(" ".join(map(str, matrix[i])).strip())


if __name__ == "__main__":
    main()
