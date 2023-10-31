from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n, m = [int(x) for x in input().split()]
    board = [[cell for cell in input()] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == ".":
                if (i + j) % 2:
                    board[i][j] = "W"
                else:
                    board[i][j] = "B"
        print("".join(board[i]))


if __name__ == "__main__":
    main()
