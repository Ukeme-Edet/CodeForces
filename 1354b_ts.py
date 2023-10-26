from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        l = r = 0
        met, cur_min = 0, float("inf")
        char_count = {"1": 0, "2": 0, "3": 0}
        while r < len(s):
            char_count[s[r]] += 1
            if char_count[s[r]] == 1:
                met += 1
            if met == 3:
                while char_count[s[l]] > 1:
                    char_count[s[l]] -= 1
                    l += 1
                cur_min = min(cur_min, r - l + 1)
                char_count[s[l]] -= 1
                l += 1
                met -= 1
            r += 1
        print(cur_min if cur_min != float("inf") else 0)


if __name__ == "__main__":
    main()
