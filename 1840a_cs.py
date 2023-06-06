def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        result = ""
        last = 0
        i = 1
        while i < len(s):
            if s[last] == s[i]:
                result += s[last]
                last = i + 1
                i += 1
            i += 1
        print(result)


if __name__ == "__main__":
    main()
