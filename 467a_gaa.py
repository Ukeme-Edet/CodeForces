def main():
    n = int(input())
    count = 0
    for _ in range(n):
        p, q = map(int, input().split())
        if q - p > 1:
            count += 1
    print(count)


if __name__ == "__main__":
    main()
