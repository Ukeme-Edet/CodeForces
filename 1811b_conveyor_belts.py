def getShell(n, x, y):
    shellx = (n / 2) - x
    shelly = (n / 2) - y

    if shellx < 0:
        shellx = abs(shellx + 1)
    if shelly < 0:
        shelly = abs(shelly + 1)
    return max(shellx, shelly)


def main():
    t = int(input())
    for _ in range(t):
        n, x1, y1, x2, y2 = map(int, input().split(" "))
        energy = getShell(n, x2, y2) - getShell(n, x1, y1)
        print(int(abs(energy)))


if __name__ == "__main__":
    main()
