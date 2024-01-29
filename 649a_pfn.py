from sys import stdin, stdout


def input():
    return stdin.readline().strip()


def print(string):
    return stdout.write(str(string) + "\n")


def main():
    n = int(input())
    a = sorted([int(_) for _ in input().split()], reverse=True)
    c = 0
    for i in range(n):
        ab = bin(a[i])[2:]
        if ab.count("1") == 1 and ab[0] == "1":
            break
    if i == n - 1 and (ab.count("1") != 1 or ab[0] != "1"):
        print(f"1 {n}")
        return
    for j in range(i, -1, -1):  
        if a[j] % a[i] == 0:
            c += 1
    print(f"{a[i]} {c}")


if __name__ == "__main__":
    main()
