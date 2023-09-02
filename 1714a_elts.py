from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, h, m = [int(x) for x in input().split()]
        alarms = [[int(y) for y in input().split()] for z in range(n)]
        alarms.sort(key=lambda x: (x[0], x[1]))
        for alarm in alarms:
            if alarm[0] >= h and (alarm[1] >= m or alarm[0] > h):
                hs = alarm[0] - h
                ms = alarm[1] - m
                if ms < 0:
                    hs -= 1
                    ms += 60
                print(f"{hs} {ms}")
                break
        else:
            hs = alarms[0][0] + 24 - h
            ms = alarms[0][1] - m
            if ms < 0:
                hs -= 1
                ms += 60
            print(f"{hs} {ms}")


if __name__ == "__main__":
    main()
