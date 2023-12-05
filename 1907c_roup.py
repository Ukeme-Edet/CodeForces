from collections import Counter, defaultdict
from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        char_dict = defaultdict(int, Counter(s))
        rem = 0
        for char in char_dict:
            if char_dict[char] > n // 2:
                rem += 2 * char_dict[char] - n
        print(rem if rem else n % 2)


if __name__ == "__main__":
    main()
