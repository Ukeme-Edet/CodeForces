from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    _ = int(input())
    x = [int(x) for x in input().split()]
    q = int(input())
    m = []
    for i in range(q):
        m.append(int(input()))
    x.sort()
    shop_count_arr = [0 for _ in range(x[-1] + 1)]
    shop_count, last_i = len(x), len(x) - 1
    for coin in range(x[-1], x[0] - 1, -1):
        if coin < x[last_i] and last_i > 0:
            while coin < x[last_i] and last_i > 0:
                shop_count -= 1
                last_i -= 1
        shop_count_arr[coin] = shop_count
    for i in m:
        if i > x[-1]:
            print(len(x))
        else:
            print(shop_count_arr[i])


if __name__ == "__main__":
    main()
