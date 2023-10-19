from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n, a, b = [int(x) for x in input().split()]
        s = input()
        if b >= 0:
            print(n * (a + b))
            continue
        css = {"1": [], "0": []}
        cc = 1
        for i in range(1, n):
            if s[i] == s[i - 1]:
                cc += 1
            else:
                css[s[i - 1]].append(cc)
                cc = 1
        if n > 1 and cc:
            css[s[i]].append(cc)
        least = "0" if len(css["0"]) < len(css["1"]) else "1"
        cost = 0
        for sub in css[least]:
            cost += a * sub + b
        print(cost + ((n - sum(css[least])) * a + b))


if __name__ == "__main__":
    main()
