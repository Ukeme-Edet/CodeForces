from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    persons = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
    i = 0
    while n > 5 * 2**i:
        n -= 5 * 2**i
        i += 1
    print(persons[(n - 1) // 2**i])


if __name__ == "__main__":
    main()
