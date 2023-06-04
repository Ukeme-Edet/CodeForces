from math import ceil


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split(" "))
        a = [0 for _ in range(n)]
        for i in range(n):
            if sum(a[0:i+1]) < ceil((i+1)/k):
                a[i] = 1
            if sum(a[-1:-i-2:-1]) < ceil((i+1)/k):
                a[-i-1] = 1
        print(sum(a))


if __name__ == "__main__":
    main()
