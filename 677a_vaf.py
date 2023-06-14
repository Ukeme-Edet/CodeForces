import math


def main():
    n, h = map(int, input().split())
    a = list(map(int, input().split()))
    a = [math.ceil(x / h) for x in a]
    print(sum(a))


if __name__ == "__main__":
    main()
