def main():
    q = int(input())
    for _ in range(q):
        n, t = map(int, input().split(" "))
        a = list(map(int, input().split(" ")))
        b = list(map(int, input().split(" ")))
        result = -1
        i = 0
        while i < n:
            if a[i] <= t:
                if result < 0:
                    result = 0
                elif b[result] < b[i]:
                    result = i
            i += 1
            t -= 1
        print(result + 1 if result > -1 else result)


if __name__ == "__main__":
    main()
