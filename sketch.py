def main():
    t = int(input())
    for _ in range(t):
        group_sizes = [[int(x), int(input())] for x in range(2, 7)]
        group_sizes = [x for x in group_sizes if x[1] != 0]
        group_sizes.sort(key=lambda x: x[0], reverse=True)
        tables = []
        l, r = 0, len(group_sizes) - 1
        while l <= r:
            table, capacity = [], 0
            while capacity + group_sizes[l][0] <= 8 and group_sizes[l][1] > 0:
                capacity += group_sizes[l][0]
                table.append(group_sizes[l][0])
                group_sizes[l][1] -= 1
            while capacity + group_sizes[r][0] <= 8 and group_sizes[r][1] > 0:
                capacity += group_sizes[r][0]
                table.append(group_sizes[r][0])
                group_sizes[r][1] -= 1
            temp = capacity
            if capacity > 6:
                capacity = 8
            else:
                capacity = 6
            tables.append([capacity, table, capacity - temp])
            if group_sizes[l][1] == 0:
                l += 1
            if group_sizes[r][1] == 0:
                r -= 1
        print(tables)


if __name__ == "__main__":
    main()
