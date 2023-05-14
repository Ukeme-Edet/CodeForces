def main():
    s = list(input())
    count = 0
    hash_map = {}
    for i in range(len(s)):
        if s[i] in hash_map:
            count += hash_map[s[i]]
            continue
        i_count = 0
        for j in range(len(s)):
            if s[i] == s[j]:
                i_count += 1
        count += i_count
        hash_map[s[i]] = i_count
    print(count)


if __name__ == "__main__":
    main()
