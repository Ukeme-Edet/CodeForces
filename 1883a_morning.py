from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        initial, seconds = 1, 0
        pin = input()
        for i in range(4):
            digit = int(pin[i])
            if digit == 0:
                digit = 10
            seconds += abs(digit - initial) + 1
            initial = digit
        print(seconds)


if __name__ == "__main__":
    main()
