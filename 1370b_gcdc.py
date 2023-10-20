from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = [[int(x), i] for i, x in enumerate(input().split())]
        a.sort(key=lambda x: x[0] % 2)
        pc = 0
        for i in range(0, 2 * n, 2):
            if a[i][0] % 2 == a[i + 1][0] % 2:
                print(f"{a[i][1] + 1} {a[i + 1][1] + 1}")
                pc += 1
            if pc == n - 1:
                break


if __name__ == "__main__":
    main()
