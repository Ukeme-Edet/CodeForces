def main():
    k, n, w = map(int, input().split(" "))
    debt = int(((w + 1) * (w / 2)) * k) - n
    if debt < 0:
        debt = 0
    print(debt)


if __name__ == "__main__":
    main()
