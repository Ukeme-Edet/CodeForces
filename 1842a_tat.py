def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        a = [int(x) for x in input().split()]
        b = [int(x) for x in input().split()]
        if sum(a) > sum(b):
            print("Tsondu")
        elif sum(a) < sum(b):
            print("Tenzing")
        else:
            print("Draw")


if __name__ == "__main__":
    main()
