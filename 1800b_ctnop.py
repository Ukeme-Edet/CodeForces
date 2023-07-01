from sys import stdin, stdout
from collections import defaultdict


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input()
        upper_dict, lower_dict = defaultdict(int), defaultdict(int)
        for i in range(n):
            if s[i].isupper() and s[i] not in upper_dict:
                upper_dict[s[i]] = s.count(s[i])
            elif s[i].islower() and s[i] not in lower_dict:
                lower_dict[s[i]] = s.count(s[i])
        for key in upper_dict:
            if k < 1:
                break
            if key.lower() in lower_dict:
                count = (max(upper_dict[key], lower_dict[key.lower(
                )]) - min(upper_dict[key], lower_dict[key.lower()])) // 2
                count = min(k, count)
                if upper_dict[key] > lower_dict[key.lower()]:
                    upper_dict[key] -= count
                    lower_dict[key.lower()] += count
                else:
                    lower_dict[key.lower()] -= count
                    upper_dict[key] += count
                k -= count
            else:
                if upper_dict[key] // 2 > 0:
                    lower_dict[key.lower()] = min(upper_dict[key] // 2, k)
                    upper_dict[key] -= lower_dict[key.lower()]
                    k -= lower_dict[key.lower()]
        for key in lower_dict:
            if k < 1:
                break
            if key.upper() in upper_dict:
                count = (max(upper_dict[key.upper()], lower_dict[key]) -
                         min(upper_dict[key.upper()], lower_dict[key])) // 2
                count = min(k, count)
                if upper_dict[key.upper()] > lower_dict[key]:
                    upper_dict[key.upper()] -= count
                    lower_dict[key] += count
                else:
                    lower_dict[key] -= count
                    upper_dict[key.upper()] += count
                k -= count
            else:
                if lower_dict[key] // 2 > 0:
                    upper_dict[key.upper()] = min(lower_dict[key] // 2, k)
                    lower_dict[key] -= upper_dict[key.upper()]
                    k -= upper_dict[key.upper()]
        pairs = 0
        for key in upper_dict:
            if key.lower() in lower_dict:
                pairs += min(upper_dict[key], lower_dict[key.lower()])
        print(pairs)


if __name__ == "__main__":
    main()
