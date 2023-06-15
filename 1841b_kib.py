def main():
    t = int(input())
    for _ in range(t):
        q = int(input())
        x = list(map(int, input().split()))
        result = ["1"]
        increasing = True
        last = x[0]
        for i in range(1, q):
            if increasing:
                if x[i] >= last:
                    result.append("1")
                    last = x[i]
                elif x[i] <= x[0]:
                    increasing = False
                    result.append("1")
                    last = x[i]
                else:
                    result.append("0")
            else:
                if x[i] >= last and x[i] <= x[0]:
                    result.append("1")
                    last = x[i]
                else:
                    result.append("0")
        print("".join(result))


if __name__ == "__main__":
    main()
