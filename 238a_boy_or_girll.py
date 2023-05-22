def main():
    name = input()
    char_set = set()
    for char in name:
        char_set.add(char)
    if len(char_set) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")


if __name__ == "__main__":
    main()
