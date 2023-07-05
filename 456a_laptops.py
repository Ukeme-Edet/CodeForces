from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    laptops = []
    for _ in range(n):
        laptops.append([int(x) for x in input().split()])
    laptops.sort(key=lambda x: x[0])
    for i in range(n-1):
        if laptops[i][1] > laptops[i+1][1]:
            print("Happy Alex")
            return
    print("Poor Alex")


if __name__ == "__main__":
    main()
