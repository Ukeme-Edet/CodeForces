def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        operations = 0
        negative = False
        for i in range(n):
            if a[i] < 0 and not negative:
                negative = True
                operations += 1
            elif a[i] > 0 and negative:
                negative = False
        max_sum = sum(list(map(abs, a)))
        print(max_sum, operations)


if __name__ == "__main__":
    main()
