def main():
    _, a, d = int(input()), 0, 0
    s = input()
    for char in s:
        if char == "A":
            a += 1
        else:
            d += 1
    if a > d:
        print("Anton")
    elif d > a:
        print("Danik")
    else:
        print("Friendship")


if __name__ == "__main__":
    main()
