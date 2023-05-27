def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split(" ")))
        if n < 4 and a[1] % 2 != 0:
            print(-1)
            continue
        if sum(a[1:n-1]) / (n-2) == 1:
            print(-1)
            continue
        even = [x for x in a[1:n-1] if x % 2 == 0]
        odd = [x for x in a[1:n-1] if x % 2 != 0]
        total = sum(even) / 2 + (((sum(odd) + len(odd)) / 2) - len(odd))
        total += len(odd)
        print(int(total))


if __name__ == "__main__":
    main()
