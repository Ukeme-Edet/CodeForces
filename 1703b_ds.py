from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        strings = []
        part_hash = {}
        res = ""
        for _ in range(n):
            string = input()
            part_hash[string] = True
            strings.append(string)
        for i in range(n):
            for j in range(1, len(strings[i])):
                if strings[i][:j] in part_hash and strings[i][j:] in part_hash:
                    res += "1"
                    break
            else:
                res += "0"
        print(res)


if __name__ == "__main__":
    main()
