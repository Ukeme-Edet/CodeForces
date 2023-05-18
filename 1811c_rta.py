def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = list(map(int, input().split(" ")))
        a = []
        for i in range(n):
            if i == 0:
                a.append(b[i], b[i +1])
            elif b[i] 


if __name__ == "__main__":
    main()

# 11
# 5
# 3 4 4 5
# 4
# 2 2 1
# 5
# 0 0 0 0
# 6
# 0 3 4 4 3
# 2
# 10
# 4
# 3 3 3
# 5
# 4 2 5 5
# 4
# 3 3 3
# 4
# 2 1 0
# 3
# 4 4
# 6
# 8 1 3 5 10
