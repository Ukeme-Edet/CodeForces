from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        s = input()
        cpq, spq, tr = [], [], {}
        i = 0
        while i < len(s):
            if s[i].lower() == "b":
                if s[i] == "b":
                    if spq:
                        tr[spq.pop()] = i
                else:
                    if cpq:
                        tr[cpq.pop()] = i
                tr[i] = i
                i += 1
                continue
            if s[i].islower():
                spq.append(i)
            else:
                cpq.append(i)
            i += 1
        for i in range(len(s)):
            stdout.write(s[i]) if i not in tr else ""
        print("")


if __name__ == "__main__":
    main()
