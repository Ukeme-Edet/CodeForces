def main():
    number_of_cows = int(input())
    cows = []
    x1, x2, y1, y2 = 0, 0, 0, 0
    for _ in range(number_of_cows):
        cows.append(list(map(int, input().split(" "))))
        if cows[-1][0] < x1:
            x1 = cows[-1][0]
        if cows[-1][0] > x2:
            x2 = cows[-1][0]
        if cows[-1][1] < y1:
            y1 = cows[-1][1]
        if cows[-1][1] > y2:
            y2 = cows[-1][1]
    number_of_steps = 0
    graph = [[0 for _ in range(x2 + 1)] for _ in range(y2 + 1)]
    for cow in cows:
        graph[cow[1]][cow[0]] = 1
    start_point = [cows[0][1] - 1, cows[0][0]]
    end_point = [cows[0][1], cows[0][0] - 1]
    # while start_point[0] != end_point[0] or start_point[1] != end_point[1]:

    print(number_of_steps + 1)


if __name__ == "__main__":
    main()
