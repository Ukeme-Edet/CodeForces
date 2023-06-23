def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        sum = 0
        while n > 0:
            sum += n
            n >>= 1
        print(sum)


if __name__ == "__main__":
    main()
