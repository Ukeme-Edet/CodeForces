import math


def main():
    n, m, a = map(int, input().split(" "))
    x, y = math.ceil(n / a), math.ceil(m / a)
    print(x * y)


if __name__ == "__main__":
    main()
