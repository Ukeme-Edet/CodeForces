from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    direction = input()
    string = input()
    keyboard = "qwertyuiopasdfghjkl;zxcvbnm,./"
    result = ""
    if direction == "R":
        for i in string:
            result += keyboard[keyboard.index(i) - 1]
    else:
        for i in string:
            result += keyboard[keyboard.index(i) + 1]
    print(result)


if __name__ == "__main__":
    main()
