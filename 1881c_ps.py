from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        i = 0
        matrix = [[x for x in input()] for _ in range(n)]
        moves = 0
        while i < n // 2:
            j = i
            while j < n - i - 1:
                val = get_max(matrix, i, j, n)
                moves += val - ord(matrix[i][j])
                moves += val - ord(matrix[j][n - i - 1])
                moves += val - ord(matrix[n - i - 1][n - j - 1])
                moves += val - ord(matrix[n - j - 1][i])
                j += 1
            i += 1
        print(moves)


def get_max(matrix, i, j, n):
    return max([ord(matrix[i][j]), ord(matrix[j][n - i - 1]), ord(matrix[n - i - 1][n - j - 1]), ord(matrix[n - j - 1][i])])


if __name__ == "__main__":
    main()
