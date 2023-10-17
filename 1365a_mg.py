from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        matrix = [input().split() for _ in range(n)]
        fr, fc = 0, 0
        for i in range(n):
            if "1" not in matrix[i]:
                fr += 1
        for j in range(m):
            if all(matrix[i][j] == "0" for i in range(n)):
                fc += 1
        print("Ashish" if min(fr, fc) % 2 else "Vivek")


if __name__ == "__main__":
    main()
