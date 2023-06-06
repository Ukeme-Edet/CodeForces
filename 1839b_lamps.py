def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lamps = [["off"] for _ in range(n)]
        for i in range(n):
            lamps[i][1:3] = (list(map(int, input().split(" "))))
        lamps.sort(key=lambda x: x[2], reverse=True)
        new_lamps = []
        for i in range(n//2):
            new_lamps.append(lamps[i])
            new_lamps.append(lamps[n//2+i])
        if n % 2 == 1:
            new_lamps.append(lamps[-1])
        lamps = new_lamps
        print(lamps)
        points = 0
        on_lamps = 0
        for i in range(n):
            if lamps[i][0] == "off":
                points += lamps[i][2]
                on_lamps += 1
                for j in range(n):
                    if lamps[j][1] <= on_lamps:
                        lamps[j][0] = "broken"
        print(points)


if __name__ == "__main__":
    main()
