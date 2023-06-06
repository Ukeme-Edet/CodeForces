import math


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        max_dishes = int(math.ceil((n + 1) / 2))
        if k > max_dishes:
            print(max_dishes + 1)
            continue
        print(2 ** k)


if __name__ == "__main__":
    main()
