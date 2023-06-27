from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    lucky_numbers = [4, 7, 44, 47, 74, 77,
                     444, 447, 474, 477, 744, 747, 774, 777]
    for lucky_number in lucky_numbers:
        if n % lucky_number == 0:
            print("YES")
            return
    print("NO")


if __name__ == "__main__":
    main()
