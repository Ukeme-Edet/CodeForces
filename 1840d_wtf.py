def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        l, r = 0, 1000000000
        while l < r:
            mid = (l + r) // 2
            carver = a[0] + mid
            used = 1
            for j in range(n):
                if abs(a[j] - carver) > mid:
                    used += 1
                    carver = a[j] + mid
            if used <= 3:
                r = mid
            else:
                l = mid + 1
        print(r)


if __name__ == "__main__":
    main()
