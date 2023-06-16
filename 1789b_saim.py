def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = list(input())
        started, printed = False, False
        i = 0
        while i < n//2:
            if s[i] != s[-1-i] and not started:
                started = True
                while s[i] != s[-1-i] and i < n//2:
                    i += 1
            elif s[i] != s[-1-i] and started:
                print("No")
                printed = True
                break
            i += 1
        if not printed:
            print("Yes")


if __name__ == "__main__":
    main()
