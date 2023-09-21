from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        grid = [input() for _ in range(10)]
        scores = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
        score = 0
        for i in range(10):
            for j in range(10):
                if grid[i][j] == "X":
                    score += scores[shell(i + 1, j + 1)]
        print(score)


def shell(x, y):
    if x > 5:
        x = 10 - x + 1
    if y > 5:
        y = 10 - y + 1
    return min(x, y)


if __name__ == "__main__":
    main()
