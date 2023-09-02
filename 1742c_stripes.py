from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        grid, c = [], 0
        while c < 8:
            s = input()
            if s == "":
                continue
            c += 1
            grid.append(s)
        print(check_last(grid))


def check_last(grid):
    return check_cols(grid) or check_rows(grid)


def check_cols(grid):
    for i in range(8):
        col = set([grid[j][i] for j in range(8)])
        if len(col) == 1 and "." not in col:
            return col.pop()
    return None


def check_rows(grid):
    for row in grid:
        if len(set(row)) == 1 and "." not in row:
            return row[0]
    return None


if __name__ == "__main__":
    main()
