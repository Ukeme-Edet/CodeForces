def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        total = 0
        last = ""
        segments = 0
        for i in range(0, n, 2):
            if s[i] != s[i+1]:
                total += 1
            elif s[i] == s[i+1] and s[i] != last:
                segments += 1
                last = s[i]
        if segments == 0:
            segments = 1
        print(total, segments)


if __name__ == "__main__":
    main()
