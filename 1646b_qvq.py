def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        a.sort()
        solved = False
        i = 1
        diff = sum(a[:i+1]) - sum(a[-i:])
        while i <= n//2:
            if diff < 0:
                solved = True
                break
            i += 1
            diff -= (a[-i] - a[i])
        if solved:
            print("YES")
            continue
        print("NO")


if __name__ == "__main__":
    main()
