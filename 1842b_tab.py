def main():
    t = int(input())
    for _ in range(t):
        n, x = map(int, input().split())
        books = [
            [int(x) for x in input().split()],
            [int(x) for x in input().split()],
            [int(x) for x in input().split()]
        ]
        k = 0
        for i in range(3):
            for j in range(n):
                if x | books[i][j] != x:
                    break
                k |= books[i][j]
        if k == x:
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
