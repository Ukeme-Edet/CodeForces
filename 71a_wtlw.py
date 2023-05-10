def main():
    number_of_words = int(input())
    for _ in range(number_of_words):
        word = input()
        word_length = len(word)
        if len(word) > 10:
            print(f"{word[0]}{word_length - 2}{word[word_length - 1]}")
            continue
        print(word)


if __name__ == "__main__":
    main()
