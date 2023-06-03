def main():
    n = input()
    lucky_count = 0
    for digit in n:
        if digit == "7" or digit == "4":
            lucky_count += 1
    lucky_count = str(lucky_count)
    for digit in lucky_count:
        if digit != "7" and digit != "4":
            print("NO")
            return
    print("YES")


if __name__ == "__main__":
    main()
