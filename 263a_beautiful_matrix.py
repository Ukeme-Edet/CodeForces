def main():
    matrix = []
    for i in range(5):
        matrix.append(list(map(int, input().split(" "))))
        if 1 in matrix[len(matrix) - 1]:
            y = i
            x = matrix[len(matrix) - 1].index(1)
    steps = 0
    while True:
        if x == 2 and y == 2:
            print(steps)
            return
        elif x < 2:
            x += 1
        elif x > 2:
            x -= 1
        elif y < 2:
            y += 1
        elif y > 2:
            y -= 1
        steps += 1


if __name__ == "__main__":
    main()
