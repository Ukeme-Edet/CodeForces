from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, x = [int(x) for x in input().split()]
        a = [int(x) for x in input().split()]
        h_max, h_min = 20e9, 0
        while True:
            h_mid = h_min + (h_max - h_min) // 2
            if w_vol(a, h_mid) > x and h_max != h_mid:
                h_max = h_mid
            elif w_vol(a, h_mid) < x and h_min != h_mid:
                h_min = h_mid
            else:
                break
        print(int(h_mid))


def w_vol(a, h):
    return sum(max(0, h - a[i]) for i in range(len(a)))


if __name__ == "__main__":
    main()
