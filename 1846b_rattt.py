from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        grid = [input() for _ in range(3)]
        horizontal_win = check_horizontal(grid)
        if horizontal_win:
            print(horizontal_win)
            continue
        vertical_win = check_vertical(grid)
        if vertical_win:
            print(vertical_win)
            continue
        diagonal_win = check_diagonal(grid)
        if diagonal_win:
            print(diagonal_win)
            continue
        print("DRAW")


def check_horizontal(grid):
    for row in grid:
        if row[0] == row[1] == row[2] != ".":
            return row[0]
    return False


def check_vertical(grid):
    for column in range(3):
        if grid[0][column] == grid[1][column] == grid[2][column] != ".":
            return grid[0][column]
    return False


def check_diagonal(grid):
    if (grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]) and grid[1][1] != ".":
        return grid[1][1]
    return False


if __name__ == "__main__":
    main()
