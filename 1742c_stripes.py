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
        print("R" if check_rows(grid) else "B")


def check_rows(grid):
    for row in grid:
        if row.count("R") == 8:
            return True
    return False


if __name__ == "__main__":
    main()
