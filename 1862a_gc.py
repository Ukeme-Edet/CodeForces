from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        grid = []
        for i in range(n):
            grid.append(input())
        name = "vika"
        i = c = 0
        while i < m:
            if name[c] in [grid[j][i] for j in range(n)]:
                c += 1
                if c == 4:
                    print("YES")
                    break
            i += 1
        else:
            print("NO")


if __name__ == "__main__":
    main()
