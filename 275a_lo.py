from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    in_grid, out_grid = [], [[True, True, True], [True, True, True], [True, True, True]]
    for _ in range(3):
        in_grid.append([True if int(x) %
                       2 else False for x in input().split()])
    for i in range(3):
        for j in range(3):
            if in_grid[i][j]:
                out_grid[i][j] = not out_grid[i][j]
                if i > 0:
                    out_grid[i - 1][j] = not out_grid[i - 1][j]
                if j > 0:
                    out_grid[i][j - 1] = not out_grid[i][j - 1]
                if j < 2:
                    out_grid[i][j + 1] = not out_grid[i][j + 1]
                if i < 2:
                    out_grid[i + 1][j] = not out_grid[i + 1][j]
    for i in range(3):
        print("".join(["1" if x else "0" for x in out_grid[i]]).strip())


if __name__ == "__main__":
    main()
