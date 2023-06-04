def main():
    n = int(input())
    max_p, current = 0, 0
    for _ in range(n):
        a, b = map(int, input().split())
        current -= a
        current += b
        max_p = max(max_p, current)
    print(max_p)


if __name__ == "__main__":
    main()
