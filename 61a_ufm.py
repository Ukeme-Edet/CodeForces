from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    a = [int(x) for x in input()]
    b = [int(x) for x in input()]
    result = ""
    for i in range(len(a)):
        result += f"{a[i] ^ b[i]}"
    print(result)


if __name__ == "__main__":
    main()
