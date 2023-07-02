from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        grid = []
        for i in range(n):
            grid.append([int(x) for x in input().split()])
        if good_grid(grid):
            print("1 1")
            continue
        bad_indexes = set()
        for i in range(n):
            best_fit = grid[i].copy()
            best_fit.sort()
            for j in range(m):
                if grid[i][j] != best_fit[j]:
                    bad_indexes.add((j))
        if len(bad_indexes) > 2:
            print("-1")
            continue
        j1 = bad_indexes.pop()
        j2 = bad_indexes.pop()
        for i in range(n):
            grid[i][j1], grid[i][j2] = grid[i][j2], grid[i][j1]
        if good_grid(grid):
            print(f"{j1+1} {j2+1}")
            continue
        print("-1")


def good_grid(grid):
    for i in range(len(grid)):
        for j in range(1, len(grid[i])):
            if grid[i][j] < grid[i][j-1]:
                return False
    return True


if __name__ == "__main__":
    main()
