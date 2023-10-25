from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    k = int(input())
    s = input()
    s_dict = {}
    for i in range(len(s)):
        if s[i] in s_dict:
            s_dict[s[i]] += 1
        else:
            s_dict[s[i]] = 1
    for key in s_dict:
        if s_dict[key] % k != 0:
            print(-1)
            return
    res = ""
    for key in s_dict:
        res += key * (s_dict[key] // k)
    print(res * k)


if __name__ == "__main__":
    main()
