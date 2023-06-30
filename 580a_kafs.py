def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = c = 1
    for i in range(1, n):
        if a[i] >= a[i-1]:
            b += 1
        else:
            c = max(b, c)
            b = 1
    c = max(b, c)
    print(c)


if __name__ == "__main__":
    main()
