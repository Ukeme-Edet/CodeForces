def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        melody_map = {}
        for j in range(2, n+1):
            if s[j-2:j] not in melody_map.keys():
                melody_map[s[j-2:j]] = True
        print(len(melody_map))


if __name__ == "__main__":
    main()
