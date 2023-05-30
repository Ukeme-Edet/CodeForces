def main():
    s, upper, lower = input(), 0, 0
    for char in s:
        if char.isupper():
            upper += 1
        else:
            lower += 1
    if upper > lower:
        print(s.upper())
    else:
        print(s.lower())


if __name__ == "__main__":
    main()
