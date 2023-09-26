from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ans = [2, 3]
        next = 4
        i = 0
        while len(ans) < n:
            while (next * 3) % (ans[i] + ans[i + 1]) == 0:
                next += 1
            ans.append(next)
            next += 1
            i += 1
        print(" ".join([str(x) for x in ans[:n]]).strip(" "))


if __name__ == "__main__":
    main()
