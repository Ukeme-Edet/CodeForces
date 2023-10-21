from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    cashes = 0
    cus_dict = {}
    for _ in range(n):
        cus = input()
        if cus not in cus_dict:
            cus_dict[cus] = 1
        else:
            cus_dict[cus] += 1
        if cus_dict[cus] > cashes:
            cashes = cus_dict[cus]
    print(cashes)


if __name__ == "__main__":
    main()
