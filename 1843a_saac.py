def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        cost = 0
        for i in range(n//2):
            cost += (a[-i-1] - a[i])
        print(cost)


if __name__ == "__main__":
    main()
