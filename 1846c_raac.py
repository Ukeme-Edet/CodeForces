from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, m, h = map(int, input().split())
        participants = []
        for j in range(n):
            contestant = [int(x) for x in input().split()]
            contestant.sort()
            points, penalty, time = 0, 0, 0
            for period in contestant:
                if time + period <= h:
                    time += period
                    points += 1
                    penalty += time
                else:
                    break
            participants.append((points, penalty, j + 1))
        participants.sort(key=lambda x: (-x[0], x[1], x[2]))
        for i in range(n):
            if participants[i][2] == 1:
                print(i + 1)
                break


if __name__ == "__main__":
    main()
