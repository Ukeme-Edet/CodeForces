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
            points, penalty = 0, 0
            if contestant[0] < h:
                points += 1
                penalty += contestant[0]
            for i in range(1, m):
                contestant[i] = contestant[i] + contestant[i - 1]
                if contestant[i] <= h:
                    points += 1
                    penalty += contestant[i]
                else:
                    break
            participants.append([contestant, points, penalty, j == 0])
        participants.sort(key=lambda x: x[2])
        participants.sort(key=lambda x: x[1], reverse=True)
        for i in range(n):
            if participants[i][3]:
                offset = 0
                if i > 0:
                    while i > offset and participants[i][1] == participants[i - offset - 1][1] and participants[i][2] <= participants[i - offset - 1][2]:
                        offset += 1
                print(i - offset + 1)
                break


if __name__ == "__main__":
    main()
