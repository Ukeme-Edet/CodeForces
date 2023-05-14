def main():
    m, n = map(int, input().split(" "))
    area = m * n
    print((area / 2).__floor__())


if __name__ == "__main__":
    main()
