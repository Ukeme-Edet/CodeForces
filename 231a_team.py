def main():
    number_of_rounds = int(input())
    number_of_solutions = 0
    for _ in range(number_of_rounds):
        polls = sum(map(int, input().split(" ")))
        if polls > 1: number_of_solutions += 1
    print(number_of_solutions)


if __name__ == "__main__":
    main()
