from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = [int(x) for x in input().split()]
        max_index = 1
        r = 0
        result = []
        for i in range(1, n):
            if p[i] > p[max_index]:
                max_index = i
        r = max_index
        result.append(p[r:])
        if r == n-1:
            for l in range(r-1, -1, -1):
                if p[l] < p[0]:
                    result.append(p[:l+1])
                    break
                else:
                    result.append([p[l]])
        else:
            result.append([p[r-1]])
            for l in range(r-2, -1, -1):
                if p[l] < p[0]:
                    result.append(p[:l+1])
                    break
                else:
                    result.append([p[l]])
        print(" ".join([" ".join([str(x) for x in y])
              for y in result]).strip())


if __name__ == "__main__":
    main()
