def main():
    num_stones = int(input())
    stones = input()
    stone_count = 0
    for i in range(1, num_stones):
        if stones[i] == stones[i-1]:
            stone_count += 1
    print(stone_count)


if __name__ == "__main__":
    main()
