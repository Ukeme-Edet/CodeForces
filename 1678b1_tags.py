def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        total = 0
        for i in range(0, n, 2):
            if s[i] != s[i+1]:
                total += 1
        print(total)


if __name__ == "__main__":
    main()
