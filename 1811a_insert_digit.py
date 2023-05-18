import math


def main():
    t = int(input())
    for _ in range(t):
        n, d = map(int, input().split(" "))
        num = input()
        for i in range(n + 1):
            if i < n and int(num[i]) < d:
                num = num[:i] + str(d) + num[i:]
                break
            elif i == n:
                num = num + str(d)
                break
        print(num)


if __name__ == "__main__":
    main()
