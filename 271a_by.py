def main():
    y = int(input())
    while True:
        y += 1
        if len(set(str(y))) == 4:
            print(y)
            break


if __name__ == "__main__":
    main()
